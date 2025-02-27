def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i + 19, min(i + 67, 96) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes