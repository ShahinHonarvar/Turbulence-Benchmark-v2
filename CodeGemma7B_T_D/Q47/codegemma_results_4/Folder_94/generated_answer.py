def palindromes_of_specific_lengths(text):
    text = text[40:95]
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 45, i + 52):
            if j <= len(text) and text[i] == text[j]:
                word = text[i:j + 1]
                if word not in palindromes:
                    palindromes.add(word)
    return palindromes