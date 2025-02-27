def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = input_string[14:95]
    palindromes = set()
    for i in range(18, 74):
        for j in range(0, len(substr) - i + 1):
            if substr[j:j + i] == substr[j:j + i][::-1] and all((char in english_letters for char in substr[j:j + i])):
                palindromes.add(substr[j:j + i])
    return palindromes