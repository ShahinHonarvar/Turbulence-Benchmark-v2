import re
    from functools import reduce

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = re.findall('[a-zA-Z]', s)
    if len(english_letters) < 4 or len(english_letters) < len(range(8)):
        return set()
    palindromes = set()
    for i in range(min(8, len(english_letters))):
        for j in range(i, min(8, len(english_letters))):
            combination = english_letters[i:j + 1]
            if is_palindrome(''.join(combination)):
                palindromes.add(reduce(lambda x, y: x.lower() + y.lower(), combination))
    return palindromes