def palindrome_of_length_n(s):
    substrings = set()
    lower_s = ''.join(filter(str.isalpha, s.lower()))
    n = len(lower_s)
    length = 73
    for i in range(n - length + 1):
        sub = lower_s[i:i + length]
        if sub == sub[::-1]:
            substrings.add(s[i:i + length])
    return substrings