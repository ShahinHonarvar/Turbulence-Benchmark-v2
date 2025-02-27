def palindromes_of_specific_lengths(text):
    start_index = 30
    end_index = 84
    valid_length_range = range(12, 21)
    palindromes = set()
    for i in range(start_index, end_index + 1):
        for j in range(i - len(text[i]), i + 1):
            substring = text[j:i + 1]
            if len(substring) in valid_length_range and substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes