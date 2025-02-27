def palindrome_of_length_n(s):
    n = 80
    if len(s) < n or any((ord(c) > 122 or (ord(c) < 97 and ord(c) > 90) or ord(c) < 48 for c in s)):
        return set()
    s = ''.join((i.lower() for i in s if i.isalpha()))
    return {s[i:n + i] for i in range(len(s) - n + 1) if s[i:n + i] == s[i:n + i][::-1]}