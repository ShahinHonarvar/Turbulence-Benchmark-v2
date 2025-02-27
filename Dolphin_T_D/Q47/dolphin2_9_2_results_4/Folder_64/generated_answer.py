def palindromes_of_specific_lengths(input_string):
    substring = input_string[:8]
    palindromes = set()
    for length in [4, 5]:
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr.lower() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes