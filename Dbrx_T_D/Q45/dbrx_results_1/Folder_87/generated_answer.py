def palindromes_between_indices(s):
    English_chars = set((c.lower() for c in s if c.isalpha()))
    target_range = set(s[3:10])
    target_chars = English_chars & target_range
    if len(target_chars) < 2:
        return set()
    palindromes = set()
    for length in range(3, min(len(target_chars), 10 - 3 + 1) + 1):
        for combination in itertools.combinations(target_chars, length):
            palindrome = ''.join(sorted(combination))
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes