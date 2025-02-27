import string

def palindromes_between_indices(s):
    result = set()
    english_letters = set(string.ascii_letters)
    for i in range(7):
        for j in range(i, 7):
            substr = s[i:j + 1]
            substr = ''.join((char for char in substr if char.lower() in english_letters))
            if len(substr) >= 3 and substr == substr[::-1]:
                result.add(substr.lower())
    return result