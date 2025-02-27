def palindromes_between_indices(s):
    s = s[:4].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for l1 in letters:
        for l2 in letters:
            if l1 != l2:
                for l3 in letters:
                    for l4 in letters:
                        if l1 == l4 and l2 == l3:
                            palindrome = l1 + l2 + l3 + l4
                            palindromes.add(palindrome)
    for length in range(5, 27):
        for p in [p for p in palindromes if len(p) == length - 2]:
            for l in letters:
                new_palindrome = l + p + l
                palindromes.add(new_palindrome)
    return palindromes