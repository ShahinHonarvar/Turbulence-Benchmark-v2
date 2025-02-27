def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes