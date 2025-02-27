from collections import defaultdict

def palindromes_of_specific_lengths(s):
    s = s[29:97].lower()
    palindrome_lengths = set(range(12, 19))
    palindromes = set()
    for length in palindrome_lengths:
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes