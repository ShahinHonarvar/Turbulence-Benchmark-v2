from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substr = s[4:7].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for palindrome in generate_palindromes(list(perm)):
                palindrome_set.add(palindrome)
    return palindrome_set

def generate_palindromes(chars):
    unique_palindromes = set()
    for p in set(permutations(chars)):
        candidate = list(p)
        if is_palindrome(candidate):
            unique_palindromes.add(''.join(candidate))
    return unique_palindromes

def is_palindrome(chars):
    return chars == chars[::-1]