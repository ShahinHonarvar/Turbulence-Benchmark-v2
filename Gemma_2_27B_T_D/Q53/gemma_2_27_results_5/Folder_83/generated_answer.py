def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 59):
        for j in range(i + 60, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result