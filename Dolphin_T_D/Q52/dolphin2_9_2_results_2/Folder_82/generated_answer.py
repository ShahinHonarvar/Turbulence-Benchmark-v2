def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    length = len(string)
    for i in range(length - 27):
        consider = string[i:i + 28]
        if consider == consider[::-1]:
            palindromes.add(consider)
    return palindromes