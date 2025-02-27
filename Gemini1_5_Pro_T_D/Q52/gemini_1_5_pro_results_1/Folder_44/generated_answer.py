def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 444):
        substring = string[i:i + 445]
        if len(substring) == 445 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes