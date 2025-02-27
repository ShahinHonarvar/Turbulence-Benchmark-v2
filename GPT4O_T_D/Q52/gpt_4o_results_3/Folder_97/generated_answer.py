def palindrome_of_length_n(s):
    n = 210
    s = ''.join(filter(str.isalpha, s)).lower()
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            substrings.add(sub)
    return substrings