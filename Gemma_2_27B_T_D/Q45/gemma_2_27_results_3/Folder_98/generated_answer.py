def palindromes_between_indices(s):
    letters = s[3:6]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    palindrome = letter1 + letter2 + letter3 + letter4 + letter4 + letter3 + letter2 + letter1
                    if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes