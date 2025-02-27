def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 11:
                result.add(substring)
    return result