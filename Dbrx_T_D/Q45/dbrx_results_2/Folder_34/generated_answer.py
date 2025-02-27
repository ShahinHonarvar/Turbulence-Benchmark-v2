import re
from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = re.findall('[a-zA-Z]', s[5:8])
    if len(eng_letters) < 2:
        return set()
    used_letters = defaultdict(int)
    for letter in eng_letters:
        used_letters[letter.lower()] += 1
    palindromes = set()
    for combo in itertools.product(set(used_letters.keys()), repeat=2):
        for i in range(used_letters[combo[0].lower()], -1, -1):
            for j in range(used_letters[combo[1].lower()], -1, -1):
                if i + j == 0:
                    continue
                candidate = ''.join((combo[k] for k in range(2))) + ''.join((combo[1 - k] for k in range(2, i + j)))
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes