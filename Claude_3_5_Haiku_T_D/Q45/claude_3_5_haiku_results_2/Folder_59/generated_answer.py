from itertools import permutations

def palindromes_between_indices(string):
    if len(string) < 10:
        return set()
    letters = [char.lower() for char in string[8:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for palindrome in generate_palindromes(list(perm)):
                unique_palindromes.add(palindrome)
    return unique_palindromes

def generate_palindromes(letters):
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for i in range(len(perm) // 2 + 1):
                candidate = perm[:i] + perm[i::-1] + perm[i + 1:]
                if len(candidate) >= 3 and candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes