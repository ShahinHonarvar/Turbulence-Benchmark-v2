def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(10, 75):
        for j in range(i - 5, i + 3):
            if j >= 0 and j < len(text) and (text[i] == text[j]):
                palindrome = text[j:i + 1]
                if len(palindrome) >= 6 and len(palindrome) <= 8 and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes