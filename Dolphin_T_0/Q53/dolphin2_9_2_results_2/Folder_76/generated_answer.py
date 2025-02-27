def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 136, len(string)):
            if string[i:j + 1] == ''.join(reversed(string[i:j + 1])):
                palindromes.add(string[i:j + 1])
    return palindromes