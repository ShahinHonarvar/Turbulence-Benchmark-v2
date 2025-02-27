def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(46, len(s) + 1):
        for i in range(len(s) - length + 1):
            string = s[i:i + length].lower()
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes