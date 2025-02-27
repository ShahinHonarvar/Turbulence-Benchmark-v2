def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(32, 72):
        for j in range(i - 20, i + 1):
            if j >= 0 and j < len(text) and (text[i] == text[j]):
                palindrome = text[j:i + 1]
                if len(palindrome) >= 21 and len(palindrome) <= 32:
                    palindromes.add(palindrome)
    return palindromes