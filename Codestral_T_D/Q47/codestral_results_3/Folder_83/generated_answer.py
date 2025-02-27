def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[75:96]
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes