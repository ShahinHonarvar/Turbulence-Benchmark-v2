from itertools import combinations
        from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        n = len(letters)
        for subset_letters in generate_letter_combinations(letters):
            if len(subset_letters) >= 3:
                for perm in get_unique_permutations(subset_letters):
                    for palindrome in create_palindromes(perm):
                        palindromes.add(palindrome)
        return palindromes

    def generate_letter_combinations(letters):
        combinations = []
        for i in range(3, len(letters) + 1):
            combinations.extend(get_combinations(letters, i))
        return combinations

    def get_combinations(letters, length):
        return [list(combo) for combo in combinations(letters, length)]

    def get_unique_permutations(letters):
        return set(permutations(letters))

    def create_palindromes(perm):
        palindromes = set()
        n = len(perm)
        for i in range(n // 2 + 1):
            left = perm[:i]
            center = perm[i:n - i] if i > 0 else perm[:n]
            right = perm[n - i:][::-1]
            candidate = ''.join(left + center + right)
            if is_palindrome(candidate) and len(candidate) >= 3:
                palindromes.add(candidate)
        return palindromes
    return generate_palindromes(letters)