def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr_length = 79 - 32 + 1
    substr = input_string[32:32 + substr_length].lower()
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if len(english_letters.intersection(candidate)) == length and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes