def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[12:93]
    for i in range(len(substring) - 41):
        palindrome = substring[i:i + 42]
        if palindrome == palindrome[::-1] and palindrome.isalpha() and (len(palindrome) <= 77):
            palindromes.add(palindrome)
        for j in range(43, 78):
            palindrome = substring[i:i + j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes