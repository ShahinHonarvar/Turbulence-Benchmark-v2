def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 93 - 33):
        for j in range(i + 33, 94):
            substring = text[i:j]
            if 34 <= len(substring) <= 54 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes