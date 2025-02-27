def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i + 109, min(i + 127, 284)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes