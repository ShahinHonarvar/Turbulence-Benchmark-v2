def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 66 and substring.isalpha():
                palindromes.add(substring)
    return palindromes