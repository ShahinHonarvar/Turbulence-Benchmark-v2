def palindromes_between_indices(text):
    text = text.lower()
    letters = ''.join(sorted(text[2:7]))
    palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        if palindrome[0] == palindrome[-1]:
            if palindrome in palindromes:
                continue
        palindromes.add(palindrome)
    return palindromes