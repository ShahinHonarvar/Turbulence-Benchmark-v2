def palindromes_of_specific_lengths(text):
    text = text.lower()
    start_index = 23
    end_index = 94
    palindromes = set()
    for length in range(17, 56):
        for i in range(start_index, end_index - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes if palindromes else set()