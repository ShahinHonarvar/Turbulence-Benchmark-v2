def palindrome_of_length_n(str):
    palindromes = set()
    for i in range(len(str) - 86):
        substring = str[i:i + 87]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes