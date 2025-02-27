def palindrome_of_length_n(text):
    palindromes = set()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and len(substring) == 38 and all((c in letters for c in substring)):
                palindromes.add(substring)
    return palindromes