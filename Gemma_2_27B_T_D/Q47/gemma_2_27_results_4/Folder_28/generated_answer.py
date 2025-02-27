def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i + 21, min(i + 33, 72)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes