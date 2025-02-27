def palindromes_of_specific_lengths(text):
    palindromes = set()
    for length in range(3, 6):
        for index in range(len(text) - length + 1):
            if text[index:index + length].lower() == text[index:index + length][::-1].lower():
                palindromes.add(text[index:index + length])
    return palindromes