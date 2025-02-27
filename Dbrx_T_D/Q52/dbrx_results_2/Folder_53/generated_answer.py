def palindrome_of_length_n(s: str) -> set:
    n = 68
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes