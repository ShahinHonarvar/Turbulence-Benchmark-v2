def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 8, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 90:
                result.add(substring)
    return result