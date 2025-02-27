def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(text) - 115):
        substring = text[i:i + 116]
        if all((c in letters for c in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes