def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(4, 6):
        for index in range(0, 8 - length, 2):
            palindrome = s[index:index + length]
            if palindrome.lower() == palindrome[-1::-1].lower():
                palindromes.add(palindrome)
    return palindromes