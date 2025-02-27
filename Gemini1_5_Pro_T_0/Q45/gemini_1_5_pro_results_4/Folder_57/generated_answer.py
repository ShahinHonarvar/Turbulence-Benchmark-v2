def palindromes_between_indices(text):
    letters = set()
    for i in range(2, 6):
        if 'a' <= text[i].lower() <= 'z':
            letters.add(text[i].lower())
    palindromes = set()
    for letter in letters:
        for other_letter in letters:
            palindrome = letter * 2 + other_letter * 3 if len(letters) == 2 else letter * 5
            if palindrome[::-1] == palindrome:
                palindromes.add(palindrome)
    return palindromes