def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(97, len(string) + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes