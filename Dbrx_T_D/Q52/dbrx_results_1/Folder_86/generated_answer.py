def palindrome_of_length_n(string, n=181):
    string = string.lower()
    string = ''.join((c for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - n + 1):
        palindrome = string[i:i + n]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes