from collections import defaultdict

def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    s = s[36:93].lower()
    for length in range(10, 36):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindrome_set.add(s[i:i + length])
    return palindrome_set