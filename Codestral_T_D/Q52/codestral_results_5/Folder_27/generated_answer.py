def palindrome_of_length_n(s: str) -> set:
    return {s[i:i + 56].lower() for i in range(len(s) - 55) if s[i:i + 56].lower() == s[i:i + 56].lower()[::-1] and s[i:i + 56].isalpha()}