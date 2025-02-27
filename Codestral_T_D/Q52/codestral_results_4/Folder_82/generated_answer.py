def palindrome_of_length_n(string):
    n = 28
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes