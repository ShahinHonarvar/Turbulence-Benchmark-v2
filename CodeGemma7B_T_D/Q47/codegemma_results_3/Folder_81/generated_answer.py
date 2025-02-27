def palindromes_of_specific_lengths(string):
    palindromes = {string[i:i + j][::-1] for i in range(12, 123) for j in range(12, 221) if j >= i and string[i:i + j].isalpha()}
    return palindromes