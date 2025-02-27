def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[10:76]
    for i in range(len(substring) - 9):
        for j in range(i + 10, len(substring) + 1):
            substring_slice = substring[i:j]
            if substring_slice.lower() == substring_slice[::-1].lower() and len(substring_slice) >= 10 and (len(substring_slice) <= 20) and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes