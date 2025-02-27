def palindromes_of_specific_lengths(string):
    substring = string[10:75]
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes