import string

def palindromes_between_indices(s):
    palindrome = set()
    s = ''.join((ch for ch in s[2:7] if ch.isalpha()))
    length = len(s)
    for i in range(length):
        for j in range(i + 3, length + 1):
            sub_s = s[i:j]
            if len(sub_s) >= 4 and sub_s.lower() in string.ascii_lowercase:
                palindrome.add(sub_s)
    return palindrome