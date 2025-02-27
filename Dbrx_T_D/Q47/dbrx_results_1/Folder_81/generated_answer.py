def palindromes_of_specific_lengths(string):
    length_range = range(12, 221)
    index_range = range(12, 123)
    palindromes = set()
    for i in index_range:
        for length in length_range:
            substring = string[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes