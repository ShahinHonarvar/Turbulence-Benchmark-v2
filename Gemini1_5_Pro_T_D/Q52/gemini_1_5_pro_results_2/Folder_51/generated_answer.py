def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 72):
        substring = string[i:i + 73]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes