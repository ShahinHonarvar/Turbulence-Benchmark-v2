def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 17):
        for j in range(i + 18, len(string)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes