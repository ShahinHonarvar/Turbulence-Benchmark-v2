def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = 392
    palindromes = set()
    str_len = len(s)
    for i in range(str_len - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes