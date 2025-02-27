def palindrome_of_length_at_least_n(argument):
    argument = argument.lower()
    palindromes = set()
    for i in range(len(argument) - 91 + 1):
        substring = argument[i:i + 91]
        if all((c.isalpha() for c in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes