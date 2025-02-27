def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(18, 66):
        for j in range(i - 22, i + 1):
            if j >= 0 and j <= len(string) - 1 and (string[j] in 'abcdefghijklmnopqrstuvwxyz'):
                palindrome = string[j:i + 1]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes