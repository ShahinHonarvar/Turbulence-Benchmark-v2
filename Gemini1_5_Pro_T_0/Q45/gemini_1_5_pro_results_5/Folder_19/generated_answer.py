def palindromes_between_indices(string):
    string = string[1:8].lower()
    letters = set(string)
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    for letter5 in letters:
                        for letter6 in letters:
                            for letter7 in letters:
                                palindrome = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7
                                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                                    palindromes.add(palindrome)
    return palindromes