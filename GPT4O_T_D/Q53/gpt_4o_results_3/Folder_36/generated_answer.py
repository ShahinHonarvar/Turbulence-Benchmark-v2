def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 144
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result