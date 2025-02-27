def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    if n < 93:
        return result
    for i in range(n - 92):
        substring = s[i:i + 93]
        if substring == substring[::-1]:
            result.add(substring)
    return result