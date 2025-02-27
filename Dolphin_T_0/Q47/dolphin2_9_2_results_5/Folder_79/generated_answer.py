def palindromes_of_specific_lengths(text):
    substring = text[1:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            section = substring[i:i + length]
            if section.lower() == section.lower()[::-1]:
                if section.isalpha():
                    palindromes.add(section)
    return palindromes