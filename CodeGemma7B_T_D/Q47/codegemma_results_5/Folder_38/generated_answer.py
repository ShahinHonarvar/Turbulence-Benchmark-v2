def palindromes_of_specific_lengths(text):
    valid_range = (18, 87)
    valid_length = range(38, 61)
    allowed_chars = set(string.ascii_lowercase)
    start_index = valid_range[0]
    end_index = valid_range[1]
    palindromes = set()
    for i in range(start_index, end_index + 1):
        for j in range(i, end_index + 1):
            substring = text[i:j + 1]
            if len(substring) in valid_length and substring.lower() == substring[::-1].lower():
                if all((char in allowed_chars for char in substring)):
                    palindromes.add(substring)
    return palindromes