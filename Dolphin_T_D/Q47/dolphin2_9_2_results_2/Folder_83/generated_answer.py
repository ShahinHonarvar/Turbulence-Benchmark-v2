def palindromes_of_specific_lengths(string):
    substring = string[75:96]
    palindromes = set()
    for i in range(7, 10):
        for j in range(len(substring) - i + 1):
            substr = substring[j:j + i]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes