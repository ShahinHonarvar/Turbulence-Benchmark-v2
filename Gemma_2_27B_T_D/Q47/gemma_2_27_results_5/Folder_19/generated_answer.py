def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 56):
        for j in range(i, 56):
            substring = text[i:j + 1]
            if len(substring) >= 3 and len(substring) <= 7 and substring.isalpha():
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes