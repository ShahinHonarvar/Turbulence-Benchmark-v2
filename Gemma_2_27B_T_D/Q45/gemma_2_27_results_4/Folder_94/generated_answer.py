def palindromes_between_indices(text):
    letters = text[3:5]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            palindrome = letter1 + letter2 + letter1.lower()
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes