def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 46):
        substring = s[i:i + 47]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes