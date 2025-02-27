def palindrome_of_length_n(s):
    results = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    target_length = 35
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            results.add(substring)
    return results