def palindrome_of_length_n(s: str) -> set:
    length = 84
    s = s.lower()
    palindromes = set()
    str_length = len(s)
    for i in range(str_length - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes