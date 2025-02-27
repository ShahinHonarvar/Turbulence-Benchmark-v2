def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 63):
        substring = string[i:i + 64].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes