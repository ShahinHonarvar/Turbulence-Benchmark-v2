def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s) - 90):
        for j in range(i + 91, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result