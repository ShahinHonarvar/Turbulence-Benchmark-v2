def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    pal = set()
    n = 255
    for i in range(len(s) - n + 1):
        if s[i:i + n] == ''.join(reversed(s[i:i + n])):
            pal.add(s[i:i + n])
    return pal