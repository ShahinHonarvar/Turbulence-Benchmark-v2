def palindrome_of_length_at_least_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 47, length):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes