def palindromes_of_specific_lengths(string):
    substring = string[28:95]
    palindromes = set()
    for length in range(38, 50):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substring[start:start + length])
    return palindromes