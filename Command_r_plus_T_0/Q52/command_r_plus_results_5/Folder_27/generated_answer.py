def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = 56
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes