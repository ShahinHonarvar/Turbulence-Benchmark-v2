import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    if len(letters) < 4:
        return set()
    letters = [ch.lower() for ch in letters]
    substrings = set()
    for i in range(4, len(letters) + 1):
        for subset in itertools.combinations(letters, i):
            subset_str = ''.join(subset)
            if subset_str == subset_str[::-1]:
                substrings.add(subset_str)
    return substrings