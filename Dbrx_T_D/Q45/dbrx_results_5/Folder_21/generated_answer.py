import re
    from collections import defaultdict

def palindromes_between_indices(s):
    pattern = re.compile('[^a-zA-Z]')
    letters = pattern.sub('', s)[1:9]
    if len(letters) < 7:
        return set()
    freq = defaultdict(int)
    for letter in letters:
        freq[letter.lower()] += 1
    permutations = [''.join(p) for i in range(7, len(letters) + 1) for p in itertools.permutations(letters, i)]
    palindromes = set()
    for perm in permutations:
        if perm == perm[::-1] and len(perm) >= 7:
            valid = True
            for letter in set(perm):
                if freq[letter] < perm.count(letter):
                    valid = False
                    break
            if valid:
                palindromes.add(perm)
    return palindromes