def palindromes_between_indices(text):
    letters = text[2:7]
    palindromes = set()
    for letter1 in letters:
        if letter1.isalpha():
            for letter2 in letters:
                if letter2.isalpha():
                    for letter3 in letters:
                        if letter3.isalpha():
                            for letter4 in letters:
                                if letter4.isalpha():
                                    for letter5 in letters:
                                        if letter5.isalpha():
                                            potential_palindrome = letter1 + letter2 + letter3 + letter4 + letter5
                                            if potential_palindrome.lower() == potential_palindrome[::-1].lower() and len(potential_palindrome) >= 3:
                                                palindromes.add(potential_palindrome)
    return palindromes