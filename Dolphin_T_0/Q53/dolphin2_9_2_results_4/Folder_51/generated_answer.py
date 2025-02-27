def palindrome_of_length_at_least_n(s):
    result = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 62):
        for j in range(i + 63, len(s_lower) + 1):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result