def palindrome_of_length_n(s):
    n = 445
    lower_s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    s_len = len(lower_s)
    for i in range(s_len - n + 1):
        sub = lower_s[i:i + n]
        if sub == sub[::-1]:
            result.add(s[i:i + n])
    return result