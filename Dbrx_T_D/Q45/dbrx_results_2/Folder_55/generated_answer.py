def palindromes_between_indices(s):
    letters = sorted(set((s[i] for i in range(3) if s[i].isalpha())))
    return {palindrome for length in range(3, len(letters) + 1) for palindrome in {''.join(permutation) for permutation in itertools.permutations(letters, length)} if palindrome == palindrome[::-1]}