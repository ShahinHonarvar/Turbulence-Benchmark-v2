def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(35, 42):
        for start_index in range(32, 80 - length + 1):
            substring = string[start_index:start_index + length]
            if substring == substring.lower():
                palindromes.add(substring)
    return palindromes