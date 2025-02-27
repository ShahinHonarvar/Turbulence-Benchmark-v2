def palindrome_of_length_at_least_n(s):
    result = set()
    s_lower = s.lower()
    for length in range(97, len(s_lower) + 1):
        for i in range(len(s_lower) - length + 1):
            substring = s_lower[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result