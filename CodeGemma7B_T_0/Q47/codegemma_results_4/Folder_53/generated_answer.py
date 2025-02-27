def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 300):
        for j in range(i - 2, i + 1):
            if j >= 0 and j < len(text) and (text[i] == text[j]):
                palindrome = text[j:i + 1]
                if len(palindrome) >= 3 and len(palindrome) <= 10:
                    palindromes.add(palindrome)
    return palindromes