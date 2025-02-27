def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 471):
        temp = string[i:i + 472]
        if temp == temp[::-1]:
            palindromes.add(temp)
    return palindromes