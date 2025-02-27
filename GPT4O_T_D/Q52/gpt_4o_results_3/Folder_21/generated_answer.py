def palindrome_of_length_n(s):
    n = 407
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            results.add(substring)
    return results