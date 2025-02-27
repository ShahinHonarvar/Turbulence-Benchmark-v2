from itertools import permutations

def is_palindrome(check_str):
    return check_str == check_str[::-1]

def palindromes_between_indices(s):
    english_letters_range = ''.join(filter(str.isalpha, s[2:10])).lower()
    palindromes_set = set()
    for p in permutations(english_letters_range):
        candidate = ''.join(p)
        if len(candidate) >= 7 and is_palindrome(candidate):
            if candidate not in palindromes_set:
                palindromes_set.add(candidate)
    return palindromes_set