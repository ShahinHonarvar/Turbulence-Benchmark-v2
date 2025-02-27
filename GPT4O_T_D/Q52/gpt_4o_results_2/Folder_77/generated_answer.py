def palindrome_of_length_n(s):
    n = 173
    lower_s = ''.join(filter(str.isalpha, s.lower()))
    result = set()
    for i in range(len(lower_s) - n + 1):
        substring = lower_s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result