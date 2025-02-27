def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(127, 289):
        for j in range(i - 141, i - 118, -1):
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes