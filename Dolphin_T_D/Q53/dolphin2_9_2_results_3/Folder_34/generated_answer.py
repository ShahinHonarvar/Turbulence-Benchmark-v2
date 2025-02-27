def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 67, len(string)):
            subsring = string[i:j + 1]
            if subsring == subsring[::-1]:
                palindromes.add(subsring)
    return palindromes