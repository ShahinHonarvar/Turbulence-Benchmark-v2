def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    str_len = len(s)
    palindrome_length = 95
    for i in range(str_len - palindrome_length + 1):
        substring = s[i:i + palindrome_length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes