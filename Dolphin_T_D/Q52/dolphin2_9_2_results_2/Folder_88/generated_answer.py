def palindrome_of_length_n(s):
    results = set()
    length = 13
    s = s.lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            results.add(substring)
    return results