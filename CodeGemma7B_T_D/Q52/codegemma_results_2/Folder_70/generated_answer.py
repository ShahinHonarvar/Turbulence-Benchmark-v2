def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 400):
        for j in range(i + 401):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes