def palindromes_between_indices(s):
    s = ''.join((c for i, c in enumerate(s) if 4 <= i <= 9 and c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s), 5, -1):
        for p in [''.join(c) for c in itertools.combinations_with_replacement(s, i // 2) if len(set(c)) <= i // 2]:
            palindrome = p + (p[::-1] if i % 2 == 0 else p[:-1][::-1])
            if len(set(palindrome)) == 1 or len(palindrome) == i:
                palindromes.add(palindrome)
    return palindromes