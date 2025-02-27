def palindromes_of_specific_lengths(text):
    text = text.lower()
    substring = text[99:296]
    palindromes = set()
    for i in range(len(substring) - 135):
        for j in range(i + 136, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes