def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] == string[j] and j - i + 1 >= 98:
                palindromes.add(string[i:j + 1])
    return palindromes