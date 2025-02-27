def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(119, 0, -1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                result.add(substring)
    return result