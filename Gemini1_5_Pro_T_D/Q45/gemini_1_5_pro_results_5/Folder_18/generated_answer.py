def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 7):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                palindrome = letter1 + letter2 + letter3
                if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes