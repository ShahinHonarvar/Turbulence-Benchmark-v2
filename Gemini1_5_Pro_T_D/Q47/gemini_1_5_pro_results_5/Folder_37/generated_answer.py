def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10):
        for j in range(i + 1, min(i + 6, 10)):
            substring = text[i:j].lower()
            if 3 <= len(substring) <= 5 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes