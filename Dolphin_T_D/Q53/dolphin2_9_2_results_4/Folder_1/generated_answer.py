def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 28):
        for j in range(i + 29, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring.lower())
    return result