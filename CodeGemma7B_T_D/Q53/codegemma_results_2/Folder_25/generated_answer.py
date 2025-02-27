def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 38:
                result.add(s[i:j].lower())
    return result