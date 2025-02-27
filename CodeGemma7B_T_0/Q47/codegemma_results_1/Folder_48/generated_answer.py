def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(155, 284):
        for j in range(i - 103, i + 121):
            if j >= len(text) or j < 0:
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes