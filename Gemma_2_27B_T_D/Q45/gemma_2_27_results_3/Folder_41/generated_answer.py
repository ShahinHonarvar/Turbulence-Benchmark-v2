def palindromes_between_indices(text):
    letters = text[2:4]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                palindrome = ''.join([letter1, letter2, letter3])
                if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes