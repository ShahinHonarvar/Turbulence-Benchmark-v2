def palindrome_of_length_at_least_n(s):
    result = set()
    n = 16
    s = ''.join(filter(str.isalpha, s.lower()))
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result