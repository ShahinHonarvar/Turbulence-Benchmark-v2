import string

def palindromes_between_indices(s):
    palindromes = set()
    for start in range(7, min(10, len(s))):
        for end in range(start + 3, min(10, len(s) + 1)):
            substring = s[start:end].lower()
            if set(substring).issubset(string.ascii_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes