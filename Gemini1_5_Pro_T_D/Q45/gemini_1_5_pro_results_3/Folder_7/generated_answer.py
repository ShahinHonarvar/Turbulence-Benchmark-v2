from collections import Counter
  import itertools

def palindromes_between_indices(string):
    s = string[1:10].lower()
    letters = [l for l in s if ord('a') <= ord(l) <= ord('z')]
    cnt = Counter(letters)
    result = set()
    for length in range(7, len(letters) + 1):
        for candidate in itertools.permutations(letters, length):
            word = ''.join(candidate)
            if word[::-1] == word and (length % 2 == 0 or (length % 2 == 1 and any((v % 2 == 1 for v in cnt.values())))):
                result.add(word)
    return result