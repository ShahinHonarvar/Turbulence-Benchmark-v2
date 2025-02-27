def palindrome_of_length_n(string, n=4):
    palindromes = set()
    string = ''.join((i.lower() for i in string if i.isalpha()))
    for i in range(len(string) - n + 1):
        if string[i:i + n] == string[i:i + n][::-1]:
            palindromes.add(string[i:i + n])
    return palindromes