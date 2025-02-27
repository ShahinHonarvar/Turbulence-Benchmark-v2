def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[12:122 + 1]
    for i in range(len(substring) - 11):
        for j in range(i + 12, len(substring) + 1):
            substring_segment = substring[i:j]
            if substring_segment.isalpha() and substring_segment.lower() == substring_segment[::-1].lower() and (12 <= len(substring_segment) <= 220):
                palindromes.add(substring_segment)
    return palindromes