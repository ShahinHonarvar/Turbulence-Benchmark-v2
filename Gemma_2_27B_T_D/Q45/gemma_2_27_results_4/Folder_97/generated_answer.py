def palindromes_between_indices(s):
    letters = set(s[0:5].lower())
    palindromes = set()
    for l in letters:
        if l * 3 in palindromes:
            continue
        palindromes.add(l * 3)
    for l1 in letters:
        for l2 in letters:
            if l1 == l2:
                continue
            palindrome = l1 + l2 + l2 + l1
            if palindrome in palindromes:
                continue
            palindromes.add(palindrome)
    return palindromes