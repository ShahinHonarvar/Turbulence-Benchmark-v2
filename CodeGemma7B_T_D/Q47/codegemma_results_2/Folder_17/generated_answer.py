def palindromes_of_specific_lengths(word):
    result = set()
    for i in range(22, 96):
        for j in range(i + 52, i + 56):
            sector_of_string = word[i:j].lower()
            if sector_of_string == sector_of_string[::-1] and sector_of_string.isalpha():
                result.add(''.join(sector_of_string))
    return result