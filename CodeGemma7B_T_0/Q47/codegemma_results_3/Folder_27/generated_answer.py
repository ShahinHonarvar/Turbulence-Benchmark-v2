def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[13:99 + 1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 26, i + 29 + 1):
            if j <= len(text):
                if text[i:j] == text[j - 1:i - 1:-1]:
                    palindromes.add(text[i:j])
    return palindromes