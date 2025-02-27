def palindrome_of_length_n(str):
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes