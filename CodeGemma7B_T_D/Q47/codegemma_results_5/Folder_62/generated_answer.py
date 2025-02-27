def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[26:88].lower()
    for i in range(len(text) - 4):
        for j in range(i + 52, i + 57):
            if text[i] == text[j]:
                palindrome = text[i:j + 1]
                palindromes.add(palindrome)
    return palindromes