def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = 25
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result