def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(3, 7):
        for index in range(len(string) - length + 1):
            palindrome = string[index:index + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes