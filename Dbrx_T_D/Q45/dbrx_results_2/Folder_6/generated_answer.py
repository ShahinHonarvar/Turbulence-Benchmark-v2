import string

def find_palindromes_in_range(s):
    english_letters = string.ascii_letters
    result = set()
    for i in range(0, min(8, len(s))):
        for j in range(i, min(8, len(s))):
            combination = s[i:j + 1].lower()
            if len(combination) >= 4 and combination == combination[::-1] and all((letter in english_letters for letter in combination)):
                result.add(combination)
    return result