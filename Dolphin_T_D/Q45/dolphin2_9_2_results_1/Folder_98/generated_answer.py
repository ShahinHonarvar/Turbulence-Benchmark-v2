from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(string):
    length = len(string)
    if length < 6:
        return set()
    substring = string[2:6]
    substring_set = set(substring.lower())
    ascii_lowercase_set = set(ascii_lowercase)
    intersection_set = substring_set & ascii_lowercase_set
    if len(intersection_set) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(intersection_set, length):
            palindrome = ''.join(perm)
            reverse_palindrome = palindrome[::-1]
            if palindrome.lower() == reverse_palindrome.lower():
                palindromes.add(palindrome.lower())
    return palindromes