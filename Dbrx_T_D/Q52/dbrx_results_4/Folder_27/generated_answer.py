def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 56, len(s) + 1) if s[i:j] == s[i:j][::-1]}