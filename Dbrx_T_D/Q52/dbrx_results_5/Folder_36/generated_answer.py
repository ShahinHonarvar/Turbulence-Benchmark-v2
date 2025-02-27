def palindrome_of_length_n(string, length=338):
    palindromes = set()
    for i in range(len(string) - length + 1):
        palindrome = string[i:i + length]
        if palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha():
            palindromes.add(palindrome)
    return palindromes