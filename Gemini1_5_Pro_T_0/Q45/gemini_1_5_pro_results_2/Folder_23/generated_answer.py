import re
  from itertools import permutations

def palindromes_between_indices(string: str) -> set[str]:
    letters = ''.join(sorted(re.sub('[^a-zA-Z]', '', string[0:7])))
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for p in permutations(letters, i):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result