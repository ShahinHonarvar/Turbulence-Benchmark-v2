def palindrome_of_length_at_least_n(text):
    s = text.lower()
    if len(s) < 88:
        return set()
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 88:
                result.add(substring)
    return result