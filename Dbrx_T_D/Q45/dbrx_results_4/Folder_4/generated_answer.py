import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    palindromes = set()
    for i in range(3, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if all((letter in english_letters for letter in substring)):
                if substring == substring[::-1] and len(substring) >= 7:
                    palindromes.add(substring)
    return palindromes