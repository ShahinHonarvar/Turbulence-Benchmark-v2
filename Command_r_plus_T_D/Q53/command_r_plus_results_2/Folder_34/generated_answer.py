def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    candidates = set()
    for i in range(len(s) - 67):
        substr = s[i:i + 68]
        if substr == substr[::-1] and substr.isalpha():
            candidates.add(substr)
    return candidates