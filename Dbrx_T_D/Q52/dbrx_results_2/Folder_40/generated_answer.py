def palindrome_of_length_n(string):
    string = string.lower()
    n = 3
    palindromes = set()
    for i in range(len(string) - n + 1):
        if string[i:i + n] == string[i:i + n][::-1]:
            palindromes.add(string[i:i + n])
    return palindromes