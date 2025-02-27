def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 129):
        substring = s[i:i + 130]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes