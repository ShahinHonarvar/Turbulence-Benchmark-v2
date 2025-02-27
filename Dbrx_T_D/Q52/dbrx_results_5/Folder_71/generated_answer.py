from collections import defaultdict

def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    if len(s) < 78:
        return set()
    palindromes = defaultdict(set)
    for i in range(len(s) - 77):
        for j in range(i, i + 78):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes[len(s[i:j + 1])].add(s[i:j + 1])
    return palindromes[78]