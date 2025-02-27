def palindrome_of_length_at_least_n(s: str) -> set:
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 63, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result