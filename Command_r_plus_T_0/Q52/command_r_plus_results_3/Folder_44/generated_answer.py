def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = 445
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes