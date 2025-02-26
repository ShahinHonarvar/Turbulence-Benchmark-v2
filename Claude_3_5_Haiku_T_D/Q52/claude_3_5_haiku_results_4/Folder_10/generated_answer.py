def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 53):
        substring = s[start:start + 54]
        if len(substring) == 54 and substring == substring[::-1]:
            is_letters_only = all((char.isalpha() for char in substring))
            if is_letters_only:
                palindromes.add(substring)
    return palindromes