def palindrome_of_length_n(string: str) -> set[str]:
    palindromes = set()
    for i in range(len(string) - 19):
        substring = string[i:i + 20]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes