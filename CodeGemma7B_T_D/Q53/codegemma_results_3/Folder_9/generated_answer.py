def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 2, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1]:
                if len(substring) >= 95:
                    palindromes.add(substring)
    return palindromes