def palindromes_of_specific_lengths(word):
    length_range = range(34, 55)
    word = word[11:94].lower()
    palindromes = set()
    for length in length_range:
        for index in range(len(word) - length + 1):
            substring = word[index:index + length]
            if all((char.isalpha() for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes