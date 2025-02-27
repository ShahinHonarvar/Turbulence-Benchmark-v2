def palindromes_between_indices(text):
    letters = text[2:5]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    palindrome = ''.join([letter1, letter2, letter3, letter4])
                    if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes