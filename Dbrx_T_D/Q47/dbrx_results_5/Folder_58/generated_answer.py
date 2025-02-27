def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(125, 284):
        for length in range(109, 127):
            if i + length - 1 < len(string):
                palindrome = string[i:i + length].lower()
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes