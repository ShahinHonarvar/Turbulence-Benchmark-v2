def palindromes_of_specific_lengths(text):
    text = text.lower()
    start_index = 43
    end_index = 95
    palindrome_lengths = range(18, 48)
    palindrome_set = set()
    for length in palindrome_lengths:
        for i in range(start_index, end_index - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set