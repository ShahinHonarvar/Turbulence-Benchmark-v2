def palindromes_of_specific_lengths(str):
    palindromes = set()
    for i in range(11, 97):
        for j in range(45, 53):
            palindrome = str[i - j:i + j + 1]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes