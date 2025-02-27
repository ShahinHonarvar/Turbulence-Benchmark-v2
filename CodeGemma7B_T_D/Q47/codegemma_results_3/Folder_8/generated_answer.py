def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[17:73].lower()
    for i in range(len(text)):
        for j in range(i + 51, min(i + 52, len(text))):
            if text[i:j + 1] == text[j:i:-1]:
                palindromes.add(text[i:j + 1])
    return palindromes