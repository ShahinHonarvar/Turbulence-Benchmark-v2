def palindrome_of_length_n(s):
    results = set()
    length = 206
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            results.add(substring)
    return results