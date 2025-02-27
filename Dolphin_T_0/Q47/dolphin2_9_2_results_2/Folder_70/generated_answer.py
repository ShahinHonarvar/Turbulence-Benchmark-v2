import string

def palindromes_of_specific_lengths(s):
    letters = set(string.ascii_lowercase)
    palindromes = set()
    for i in range(10, 71):
        for length in range(24, 53):
            substring = s[i:i + length]
            clean_substring = ''.join([char for char in substring if char in letters])
            lower_substring = clean_substring.lower()
            if lower_substring == lower_substring[::-1]:
                palindromes.add(clean_substring)
    return palindromes