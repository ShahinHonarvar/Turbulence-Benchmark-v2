def palindromes_between_indices(text):
    substring = text[5:9]
    letters = sorted([char for char in substring if char.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes