def palindrome_of_length_n(s):
    s = s.lower()
    a = set()
    for i in range(len(s) - 62):
        if s[i:i + 63] == s[i:i + 63][::-1] and s[i:i + 63].isalpha():
            a.add(s[i:i + 63])
    return a