def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    str_len = len(s)
    for i in range(str_len - 76):
        substring = s[i:i + 87]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes