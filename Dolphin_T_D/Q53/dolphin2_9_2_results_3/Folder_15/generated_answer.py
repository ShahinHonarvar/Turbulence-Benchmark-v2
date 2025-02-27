def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 3, len(string)):
            subword = string[i:j + 1]
            if subword == subword[::-1]:
                palindromes.add(subword)
    return palindromes