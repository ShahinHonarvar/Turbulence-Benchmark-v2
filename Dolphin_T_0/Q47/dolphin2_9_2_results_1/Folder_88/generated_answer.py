def palindromes_of_specific_lengths(s):
    subString = s[11:88]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(subString) - length + 1):
            if subString[i:i + length].lower() == subString[i:i + length].lower()[::-1]:
                palindromes.add(subString[i:i + length])
    return palindromes