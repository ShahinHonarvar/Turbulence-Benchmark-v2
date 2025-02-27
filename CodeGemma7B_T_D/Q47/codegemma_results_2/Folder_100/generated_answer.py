def palindromes_of_specific_lengths(text):
    specific_substring = text[29:97].lower()
    palindromes = set()
    for start in range(len(specific_substring) - 11):
        for end in range(start + 12, start + 19):
            substring = specific_substring[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes