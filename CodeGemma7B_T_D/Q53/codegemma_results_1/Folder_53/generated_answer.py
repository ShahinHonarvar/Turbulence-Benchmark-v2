def palindrome_of_length_at_least_n(str_arg):
    """
    Description:
    """
    str_length = len(str_arg.lower())
    palindromes = set()
    for i in range(str_length):
        for j in range(i + 1, str_length + 1):
            substring = str_arg[i:j]
            if substring.isalpha() and len(substring) >= 64 and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes