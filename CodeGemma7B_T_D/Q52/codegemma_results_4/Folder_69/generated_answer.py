from collections import defaultdict

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 235):
        for j in range(i + 1, len(s) - 234):
            for k in range(j + 1, len(s) - 233):
                if s[i:j + 1] == s[k:j + 1][::-1]:
                    palindromes.add(s[i:j + 1])
    return palindromes