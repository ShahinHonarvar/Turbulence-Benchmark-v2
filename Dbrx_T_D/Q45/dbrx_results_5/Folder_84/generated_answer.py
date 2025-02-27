import re
    from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    letters = set(re.findall('[a-z]', s[4:10]))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for length in range(3, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            subset = ''.join(subset)
            if subset[0] == subset[-1] and subset[1:-1] in palindromes:
                continue
            palindromes.add(subset)
    return palindromes