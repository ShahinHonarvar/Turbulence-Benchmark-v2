def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(17, 96):
        for j in range(i - 12, i + 28):
            if j - i + 1 in range(13, 50) and text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes