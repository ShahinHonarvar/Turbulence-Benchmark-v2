from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    if len(input_string) < 9:
        return set()
    substring = input_string[3:9].lower()
    letters_only = ''.join(filter(str.isalpha, substring))
    if len(letters_only) < 7:
        return set()
    palindromes_set = set()
    for perm in permutations(letters_only, 7):
        possible_palindrome = ''.join(perm)
        if is_palindrome(possible_palindrome):
            palindromes_set.add(possible_palindrome)
    return palindromes_set