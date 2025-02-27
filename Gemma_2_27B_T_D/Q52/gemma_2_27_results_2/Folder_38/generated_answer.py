def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 37):
        substring = string[i:i + 38].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes