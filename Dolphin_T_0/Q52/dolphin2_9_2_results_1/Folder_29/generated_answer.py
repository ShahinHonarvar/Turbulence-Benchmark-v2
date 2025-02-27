def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 18):
        if string[i:i + 19] == string[i:i + 19][::-1]:
            palindromes.add(string[i:i + 19])
    return palindromes