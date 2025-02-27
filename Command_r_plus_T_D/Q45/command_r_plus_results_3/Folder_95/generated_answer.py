def palindromes_between_indices(s):
    letters = [c for c in s[7:9] if c.isalpha()]
    combinations = []
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            combinations.append(''.join(letters[i:j]))
    palindromes = set((c for c in combinations if len(c) >= 3 and c == c[::-1]))
    return palindromes