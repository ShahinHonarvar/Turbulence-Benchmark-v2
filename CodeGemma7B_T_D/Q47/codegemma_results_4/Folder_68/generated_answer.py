def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    text = ''.join((char for char in text if char.isalpha()))
    for i in range(50):
        for j in range(i, min(i + 50, 100)):
            if text[i] == text[j]:
                palindrome = text[i:j + 1]
                palindromes.add(palindrome)
    return palindromes