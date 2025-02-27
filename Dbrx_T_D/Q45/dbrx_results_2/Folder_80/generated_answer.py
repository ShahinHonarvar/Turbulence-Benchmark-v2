from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = set(s)
    palindromes = set()
    if len(letters) < 7:
        return palindromes

    def is_palindrome(s):
        return s == s[::-1]

    def generate_permutations(prefix, letters):
        if not letters:
            return [prefix]
        permutations = []
        for letter in letters:
            remaining_letters = letters.copy()
            remaining_letters.remove(letter)
            for perm in generate_permutations(prefix + letter, remaining_letters):
                permutations.append(perm)
        return permutations
    for perm in generate_permutations('', letters):
        if is_palindrome(perm):
            palindromes.add(perm)
    return palindromes