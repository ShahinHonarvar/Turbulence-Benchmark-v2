import itertools

def palindromes_between_indices(s):
    letters = s[0:7].lower()
    result = set()
    for length in range(3, len(letters) + 1):
        for letters_combo in itertools.combinations(letters, length):
            if letters_combo == letters_combo[::-1]:
                result.add(''.join(letters_combo))
    return result