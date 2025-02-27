def palindromes_of_specific_lengths(input_string):
    substring = input_string[10:93]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes