import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_uppercase)
    s = s.upper()
    palindromes = set()
    for i in range(1, 7):
        for j in range(i, 7):
            substring = s[i:j + 1]
            if len(substring) < 4:
                continue
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes