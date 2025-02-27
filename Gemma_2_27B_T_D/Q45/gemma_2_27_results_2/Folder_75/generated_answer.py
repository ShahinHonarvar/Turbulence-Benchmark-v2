def palindromes_between_indices(text):
    letters = text[2:5]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                if letter1.isalpha() and letter2.isalpha() and letter3.isalpha():
                    palindrome = letter1 + letter2 + letter3 + letter3 + letter2 + letter1
                    palindromes.add(palindrome.lower())
    return palindromes