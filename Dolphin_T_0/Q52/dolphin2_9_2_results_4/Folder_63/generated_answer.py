def palindrome_of_length_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 18 + 1):
        sub = s[i:i + 18]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes