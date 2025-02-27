def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[39:95]
    for i in range(len(substring) - 13):
        for j in range(i + 14, min(i + 53, len(substring) + 1)):
            substring_segment = substring[i:j]
            if substring_segment.lower() == substring_segment[::-1].lower() and substring_segment.isalpha():
                palindromes.add(substring_segment)
    return palindromes