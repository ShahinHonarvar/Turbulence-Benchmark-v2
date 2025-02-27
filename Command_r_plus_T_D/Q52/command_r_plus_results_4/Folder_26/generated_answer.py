def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 366 + 1):
        substring = s[i:i + 366]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes