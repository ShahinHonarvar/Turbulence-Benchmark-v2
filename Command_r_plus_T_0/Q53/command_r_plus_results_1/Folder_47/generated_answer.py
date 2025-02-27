def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes