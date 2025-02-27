def palindromes_between_indices(text):
    letters = text[4:6]
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes