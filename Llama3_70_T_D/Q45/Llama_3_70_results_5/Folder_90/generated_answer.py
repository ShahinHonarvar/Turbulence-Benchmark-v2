def palindromes_between_indices(s):
    letters = set(s[:6].lower())
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                palindrome = i + j + k + j + i
                palindromes.add(palindrome)
    return palindromes