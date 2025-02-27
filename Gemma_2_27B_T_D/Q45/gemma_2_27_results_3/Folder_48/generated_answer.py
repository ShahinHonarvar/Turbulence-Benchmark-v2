def palindromes_between_indices(text):
    letters = text[6:9]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    potential_palindrome = letter1 + letter2 + letter3 + letter4 + letter4 + letter3 + letter2 + letter1
                    if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and len(potential_palindrome) >= 4:
                        palindromes.add(potential_palindrome)
    return palindromes