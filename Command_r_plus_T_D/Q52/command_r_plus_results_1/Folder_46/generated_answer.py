def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = 464
    palindromes = set()
    str_length = len(s)
    for i in range(str_length - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes