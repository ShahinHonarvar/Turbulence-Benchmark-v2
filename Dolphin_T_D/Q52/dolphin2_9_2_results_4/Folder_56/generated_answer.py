def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join((e for e in string if e.isalpha()))
    length = 95
    n = len(string)
    palindromes = set()
    for i in range(0, n / 2):
        if string[i:i + length] == string[i:i + length][::-1]:
            palindromes.add(string[i:i + length])
    return palindromes