def palindromes_of_specific_lengths(text):
    start_index = 10
    end_index = 59
    min_length = 18
    max_length = 36
    palindromes = set()
    text = text.lower()
    for i in range(start_index, end_index + 1):
        for j in range(i + min_length, i + max_length + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes