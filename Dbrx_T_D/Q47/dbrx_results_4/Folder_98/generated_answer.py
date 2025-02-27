def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(20):
        for length in range(5, 81):
            substring = string[i:i + length]
            if len(substring) == length and substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes