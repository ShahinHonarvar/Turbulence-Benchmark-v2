def palindrome_of_length_n(string):
    string_lower = string.lower()
    palindromes = set()
    for i in range(len(string_lower) - 115):
        substring = string_lower[i:i + 116]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes