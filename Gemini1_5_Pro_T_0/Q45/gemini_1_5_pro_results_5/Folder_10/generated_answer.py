def palindromes_between_indices(text):
    letters = set()
    for i in range(6):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                palindrome = letter1 + letter2 + letter3
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes