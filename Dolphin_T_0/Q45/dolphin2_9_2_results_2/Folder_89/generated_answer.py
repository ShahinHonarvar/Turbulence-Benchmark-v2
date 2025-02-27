import itertools

def palindromes_between_indices(s):
    s5_to_s9 = [c for i, c in enumerate(s) if 5 <= i <= 9]
    s5_to_s9 = [c.lower() for c in s5_to_s9]
    length_6_palindromes = set()
    for length in range(6, len(s5_to_s9) + 1):
        for p in itertools.permutations(s5_to_s9, length):
            p = ''.join(p)
            if p == p[::-1]:
                length_6_palindromes.add(p)
    return length_6_palindromes