def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 37, min(i + 61, 84)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes