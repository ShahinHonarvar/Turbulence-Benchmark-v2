def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 40):
        if string[i:i + 41] == string[i:i + 41][::-1]:
            palindromes.add(string[i:i + 41])
    return palindromes