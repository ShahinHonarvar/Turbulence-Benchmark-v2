def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    str_len = len(s)
    for i in range(str_len):
        for j in range(i + 63, str_len + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes