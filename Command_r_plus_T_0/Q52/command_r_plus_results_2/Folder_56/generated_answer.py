def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 95 + 1):
        substring = s[i:i + 95]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes