def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 16, len(s)):
            substr = s[i:j + 1]
            if all((c.isalpha() for c in substr)):
                if substr == substr[::-1]:
                    result.add(substr)
    return result