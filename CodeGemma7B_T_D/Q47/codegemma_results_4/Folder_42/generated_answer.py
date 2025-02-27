def palindromes_of_specific_lengths(string):
    filtered_string = string[43:95].lower()
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(filtered_string) - length + 1):
            substring = filtered_string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes