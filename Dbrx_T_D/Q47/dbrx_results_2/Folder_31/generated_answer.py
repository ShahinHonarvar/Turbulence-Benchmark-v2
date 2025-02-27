def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 84):
        for length in range(37, 61):
            if i + length - 1 <= 82:
                palindrome = string[i:i + length].lower()
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes