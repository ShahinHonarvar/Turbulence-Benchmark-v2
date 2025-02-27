def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i + 21, 72):
            substring = text[i:j]
            if len(substring) > 32:
                break
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes