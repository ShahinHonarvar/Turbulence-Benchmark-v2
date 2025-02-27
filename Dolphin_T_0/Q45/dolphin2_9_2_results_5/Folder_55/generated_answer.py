import string

def palindromes_between_indices(s):
    s1 = sorted([c for c in s.lower() if c in string.ascii_lowercase])
    palindromes = set()
    for i in range(len(s1)):
        if i + 2 < len(s1):
            palindrome = s1[i:i + 3]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes