import itertools

def palindromes_between_indices(s):
    result = set()
    for i in range(1, 4):
        for j in range(i + 1, 5):
            substring = s[i:j + 1].lower()
            if len(substring) >= 4:
                letters = tuple(sorted(set(substring)))
                for combo in itertools.combinations_with_replacement(letters, len(letters)):
                    candidate = ''.join(combo)
                    if len(candidate) >= 4 and candidate == candidate[::-1]:
                        result.add(candidate)
    return result