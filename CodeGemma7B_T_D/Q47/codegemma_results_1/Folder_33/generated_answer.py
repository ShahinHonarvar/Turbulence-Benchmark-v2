def palindromes_of_specific_lengths(text):
    start = 130
    end = 295
    length_range = range(103, 159)
    palindromes = set()
    for i in range(start, end + 1):
        for length in length_range:
            substring = text[i:i + length].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes