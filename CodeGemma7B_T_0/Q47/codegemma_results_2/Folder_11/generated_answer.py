def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(24, 98):
        for j in range(i - 9, i + 1):
            if j - i + 1 >= 10 and j - i + 1 <= 36 and (text[i:j + 1] == text[i:j + 1][::-1]):
                palindromes.add(text[i:j + 1])
    return palindromes