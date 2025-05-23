def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 20):
        substring = string[i:i + 21].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes