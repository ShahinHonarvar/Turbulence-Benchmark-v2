def palindromes_between_indices(s):
    letters = set(s[1:5])
    palindromes = set()
    for i in range(5, 1000, 2):
        for letter in letters:
            palindrome = letter + ''.join((choice(letters - {letter}) for _ in range((i - 1) // 2))) + letter
            if palindrome.upper() in palindromes:
                continue
            palindromes.add(palindrome.upper())
    return {p for p in palindromes if len(set(p)) == 5}