def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 76):
        for j in range(i + 9, i + 21):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes