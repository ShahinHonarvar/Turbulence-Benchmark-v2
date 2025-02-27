def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 9, len(string) + 1):
            if string[i:j].isalpha() and string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes