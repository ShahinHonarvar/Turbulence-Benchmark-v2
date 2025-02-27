def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    n = 35
    result = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result