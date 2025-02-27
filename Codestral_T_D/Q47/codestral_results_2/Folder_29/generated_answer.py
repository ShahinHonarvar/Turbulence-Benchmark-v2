def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:95]
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes