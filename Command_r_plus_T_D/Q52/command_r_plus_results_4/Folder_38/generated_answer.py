def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 37):
        substring = s[i:i + 38]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes