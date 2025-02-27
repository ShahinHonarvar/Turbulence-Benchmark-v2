def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 28 + 1):
        for j in range(i + 28, len(string) + 1):
            if sting[i:j] == sting[i:j][::-1]:
                palindromes.add(sting[i:j])
    return palindromes