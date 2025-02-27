def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 288 - 119 + 1):
        for j in range(i + 119, min(289, i + 141) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes