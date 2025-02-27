def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(1, 10):
        for j in range(i - 2, i + 5):
            if j >= len(text) or j < 0:
                continue
            if text[i] == text[j]:
                palindrome = text[i:j + 1]
                if len(palindrome) >= 3 and len(palindrome) <= 7:
                    result.add(palindrome)
    return result