def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for i in range(18, 98 + 1):
        for j in range(31, 51 + 1):
            if i + (j - 1) <= 98 and text[i:i + j] == text[i:i + j][::-1]:
                palindromes.add(text[i:i + j])
    return palindromes