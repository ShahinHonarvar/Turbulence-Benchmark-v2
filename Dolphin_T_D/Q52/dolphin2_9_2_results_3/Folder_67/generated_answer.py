def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join(filter(str.isalpha, string))
    length = 42
    palindromes = set()
    for i in range(len(string) - length + 1):
        if string[i:i + length] == string[i:i + length][::-1]:
            palindromes.add(string[i:i + length])
    return palindromes