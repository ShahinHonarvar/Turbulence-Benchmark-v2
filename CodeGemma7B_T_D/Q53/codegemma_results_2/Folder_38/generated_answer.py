def palindrome_of_length_at_least_n(s: str) -> set[str]:
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) >= 56:
                palindrome_set.add(substring)
    return palindrome_set