def palindrome_of_length_at_least_n(aString):
    n = 42
    aString = aString.lower()
    palindromes = set()
    for i in range(len(aString)):
        for j in range(i + n - 1, len(aString)):
            subString = aString[i:j + 1]
            if subString == subString[::-1]:
                palindromes.add(subString)
    return palindromes