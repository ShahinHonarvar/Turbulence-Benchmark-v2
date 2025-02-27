import re

def palindromes_between_indices(s):
    letters = set(re.findall('[a-zA-Z]', s[0:6]))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            candidate = ''.join(sorted(combination))
            if candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes