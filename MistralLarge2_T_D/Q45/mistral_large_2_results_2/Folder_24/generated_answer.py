import itertools

def palindromes_between_indices(s):
    relevant_chars = [c for c in s[2:10] if c.isalpha()]
    permutations = set(itertools.permutations(relevant_chars))
    palindromes = set()
    for p in permutations:
        for length in range(4, len(p) + 1):
            for i in range(len(p) - length + 1):
                substring = p[i:i + length]
                if substring == substring[::-1]:
                    palindromes.add(''.join(substring))
    return palindromes