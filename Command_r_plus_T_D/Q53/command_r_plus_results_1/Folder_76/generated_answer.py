def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s) - 136):
        substr = s[i:i + 137]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result