def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(11, 97):
        for j in range(i + 45, i + 53):
            if j <= len(text):
                if text[i:j] == text[i:j][::-1]:
                    palindromes.add(text[i:j])
    return palindromes