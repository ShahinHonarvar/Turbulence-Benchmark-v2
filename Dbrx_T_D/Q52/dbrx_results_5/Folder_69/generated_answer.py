def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    return {s[i:i + 472] for i in range(len(s) - 472 + 1) if s[i:i + 472] == s[i:i + 472][::-1]}