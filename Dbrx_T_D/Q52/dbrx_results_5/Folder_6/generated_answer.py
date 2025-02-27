def palindrome_of_length_n(s: str) -> set:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 474 + 1):
        substr = s[i:i + 474].lower()
        if all((char in allowed_chars for char in substr)) and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes