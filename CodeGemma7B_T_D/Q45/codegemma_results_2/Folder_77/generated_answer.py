def palindromes_between_indices(text):
    text = text.lower().replace('[^a-z]', '')
    unique_letters = set(text[4:7])
    palindromes = set()
    for i in range(4, 7):
        for j in range(i + 4, 7):
            palindromes.add(''.join(sorted([text[i], text[j]])))
    return palindromes or {}