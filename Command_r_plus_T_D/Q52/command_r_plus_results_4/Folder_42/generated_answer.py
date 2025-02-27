def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = 279
    palindromes = set()
    string_length = len(s)
    for i in range(string_length - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes