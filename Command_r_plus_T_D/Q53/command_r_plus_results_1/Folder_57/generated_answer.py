def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes