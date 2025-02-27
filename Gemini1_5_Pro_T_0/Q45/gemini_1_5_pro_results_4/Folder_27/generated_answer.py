import re
  from collections import Counter

def palindromes_between_indices(text):
    letters = re.findall('[a-zA-Z]', text[2:9])
    counts = Counter(letters)
    middle = ''.join([l for l in counts if counts[l] % 2 == 1][:1])
    half = ''.join([l * (counts[l] // 2) for l in counts])
    permutations = set([''.join(p) for p in itertools.permutations(half)])
    return {p + middle + p[::-1] for p in permutations if len(p) > 2}