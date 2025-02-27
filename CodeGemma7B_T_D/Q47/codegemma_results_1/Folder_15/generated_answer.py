def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, min(i + 7, len(text))):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                if i >= 0 and j <= 6:
                    if len(substring) in range(3, 7):
                        palindrome = substring.lower()
                        palindromes.add(palindrome)
    return palindromes