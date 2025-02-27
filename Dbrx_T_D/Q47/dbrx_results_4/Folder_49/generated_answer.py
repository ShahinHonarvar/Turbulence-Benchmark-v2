def palindromes_of_specific_lengths(text):
    palindromes = set()
    for length in range(10, 51):
        for index in range(10, 101 - length + 1):
            if text[index:index + length].lower() == text[index:index + length][::-1].lower():
                palindromes.add(text[index:index + length])
    return palindromes