def palindrome_of_length_at_least_n(s):
    result = set()
    for length in range(76, len(s) + 1):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                result.add(s[i:i + length])
    return result