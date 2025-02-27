def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(10):
        for j in range(3, 6):
            if len(text[i:i + j]) == j and text[i:i + j] == text[i:i + j][::-1]:
                palindromes.add(text[i:i + j])
    return palindromes