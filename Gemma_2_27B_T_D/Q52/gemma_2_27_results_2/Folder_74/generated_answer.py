def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 95):
        substring = string[i:i + 96].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes