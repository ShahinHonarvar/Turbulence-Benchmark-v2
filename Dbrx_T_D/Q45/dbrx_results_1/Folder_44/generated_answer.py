from sets import Set

def palindromes_between_indices(string):
    english_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_uppercase_letters = english_lowercase_letters.upper()
    valid_characters = english_lowercase_letters + english_uppercase_letters
    palindromes = Set()
    for i in range(2, min(8, len(string))):
        for j in range(i, min(7, len(string))):
            substring = string[i:j + 1]
            substring = ''.join(filter(valid_characters.__contains__, substring))
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes