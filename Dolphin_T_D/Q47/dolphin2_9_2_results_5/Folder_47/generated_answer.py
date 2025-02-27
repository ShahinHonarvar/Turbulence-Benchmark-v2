def palindromes_of_specific_lengths(text):
    substring = text[39:95]
    result = set()
    for length in range(14, 53):
        for index in range(0, len(substring) - length + 1):
            if substring[index:index + length] == substring[index:index + length][::-1] and substring[index:index + length].isalpha():
                result.add(substring[index:index + length].lower())
    return result