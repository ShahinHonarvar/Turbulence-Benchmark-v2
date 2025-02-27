def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = s[i:j]
            if len(substring) == 18 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes