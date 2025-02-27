def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length - 78 + 1):
        substring = s[i:i + 78]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes