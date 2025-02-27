import itertools

def palindromes_between_indices(s):
    relevant_chars = [c for c in s[2:6] if c.isalpha()]
    lower_relevant_chars = [c.lower() for c in relevant_chars]
    palindromes = set()
    for length in range(4, len(lower_relevant_chars) + 1):
        for combo in itertools.combinations_with_replacement(lower_relevant_chars, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes