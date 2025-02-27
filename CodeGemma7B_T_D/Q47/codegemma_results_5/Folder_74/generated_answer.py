def palindromes_of_specific_lengths(text):
    text_lower = text.lower()
    palindromes = set()
    for i in range(30, 86):
        for j in range(i + 12, i + 21):
            palindrome = text_lower[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes