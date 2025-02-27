def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 422):
        substring = string[i:i + 423].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes