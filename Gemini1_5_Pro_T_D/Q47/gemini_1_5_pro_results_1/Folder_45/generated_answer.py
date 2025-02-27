def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i + 3, 141):
            substring = text[i:j].lower()
            if 3 <= len(substring) <= 60 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(text[i:j])
    return palindromes