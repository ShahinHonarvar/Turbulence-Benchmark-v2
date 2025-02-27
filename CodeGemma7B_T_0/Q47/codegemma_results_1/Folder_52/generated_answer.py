def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(44, 100):
        for j in range(i - 12, i + 13):
            if j - i + 1 in range(13, 43):
                if text[i:j + 1] == text[i:j + 1][::-1]:
                    palindromes.add(text[i:j + 1])
    return palindromes