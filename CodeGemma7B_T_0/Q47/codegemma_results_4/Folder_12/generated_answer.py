def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(62, 89):
        for j in range(i - 17, i + 1):
            if j < 0 or j > len(text) - 1:
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if len(palindrome) >= 18 and len(palindrome) <= 21:
                    palindromes.add(palindrome)
    return palindromes