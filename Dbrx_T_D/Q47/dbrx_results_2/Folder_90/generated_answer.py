def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(136, 152):
        if len(input_string[106:281]) < length:
            break
        for start in range(106, 281 - length + 1):
            if input_string[start:start + length].lower().rstrip().lstrip() == input_string[start:start + length].lower()[::-1].rstrip().lstrip() and all((char in english_letters for char in input_string[start:start + length].lower())):
                palindromes.add(input_string[start:start + length].lower())
    return palindromes