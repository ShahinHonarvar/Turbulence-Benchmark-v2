def palindrome_of_length_at_least_n(s):
    result = set()
    for length in range(7, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result