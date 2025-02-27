def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 8):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for letter in letters:
        palindrome = letter * 7
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes