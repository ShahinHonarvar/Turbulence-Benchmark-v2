def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = 188
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            result.add(sub)
    return result