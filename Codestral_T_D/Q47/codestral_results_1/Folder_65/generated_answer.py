def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:96]
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes