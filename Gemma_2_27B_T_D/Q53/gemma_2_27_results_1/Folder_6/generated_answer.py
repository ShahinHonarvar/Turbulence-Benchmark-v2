def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 21):
        for j in range(i + 21, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 22:
                result.add(substring)
    return result