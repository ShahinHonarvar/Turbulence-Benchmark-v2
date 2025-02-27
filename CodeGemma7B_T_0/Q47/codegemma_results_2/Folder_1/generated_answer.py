def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(15, 90):
        for j in range(i + 40, i + 73):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes