def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    substring = text[12:57]
    for i in range(len(substring) - 19):
        for j in range(i + 20, len(substring) + 1):
            substring_range = substring[i:j]
            if substring_range == substring_range[::-1]:
                if i + 20 >= 12 and i + 20 <= 21 and (j - i + 1 == 20):
                    palindromes.add(substring_range)
    return palindromes