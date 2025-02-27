def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 391):
        for j in range(i + 392, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result