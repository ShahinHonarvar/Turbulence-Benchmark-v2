def palindromes_between_indices(text):
    text = text.lower()
    text = text[2:7]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                palindrome = text[i] + text[j] + text[k]
                palindromes.add(palindrome)
    return palindromes