def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for i in range(15, 90):
        for j in range(40, 73):
            if len(text[i - j:i]) == j:
                if text[i - j:i].isalpha():
                    palindromes.add(text[i - j:i])
    return palindromes