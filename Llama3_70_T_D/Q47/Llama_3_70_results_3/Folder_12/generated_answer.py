def palindromes_of_specific_lengths(input_string):
    input_string = input_string.lower()
    substring = input_string[62:89]
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes