def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 62):
        for length in range(63, len(s) - i + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result