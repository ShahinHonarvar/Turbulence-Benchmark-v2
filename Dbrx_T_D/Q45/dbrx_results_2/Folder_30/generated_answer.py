def palindromes_between_indices(text):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 5):
        for j in range(0, 5 - i + 1):
            substring = text[0:5][j:j + i].lower()
            if len(substring) >= 4 and all((char in english_letters for char in substring)):
                palindrome = substring + ''.join(reversed(substring))
                palindromes.add(palindrome)
    return palindromes