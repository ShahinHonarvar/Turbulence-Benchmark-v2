def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(21, 63):
        for j in range(i - 21, i + 1):
            if j >= 0 and j < len(text) and (text[i - j] == text[i + j]):
                palindrome = text[i - j:i + j + 1]
                if len(palindrome) >= 22 and len(palindrome) <= 33:
                    palindromes.add(palindrome)
    return palindromes