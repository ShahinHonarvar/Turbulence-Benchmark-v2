def palindromes_of_specific_lengths():
    start = 65
    end = 99
    min_length = 26
    max_length = 33
    palindromes = set()
    current_substring = text_specification[start:end + 1]
    for length in range(min_length, max_length + 1):
        for i in range(len(current_substring) - length + 1):
            substring = current_substring[i:i + length]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes