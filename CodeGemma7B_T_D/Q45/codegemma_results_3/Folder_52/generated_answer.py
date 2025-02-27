def palindromes_between_indices(text):
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 6, len(text)):
            substring = text[i:j + 1]
            if substring.isalpha():
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes