def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes