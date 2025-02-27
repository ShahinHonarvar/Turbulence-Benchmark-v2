def palindrome_of_length_n(string, length=4):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - length + 1):
        palindrome = string[i:i + length]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes