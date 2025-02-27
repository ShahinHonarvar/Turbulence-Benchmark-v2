import string

def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c in string.ascii_lowercase for c in substring)):
                palindromes.add(substring)
    return palindromes