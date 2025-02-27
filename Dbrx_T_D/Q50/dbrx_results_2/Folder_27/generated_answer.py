import collections

def if_contains_anagrams(lines):
    anagrams = collections.defaultdict(lambda: collections.defaultdict(int))
    for line in lines:
        line = line.lower()
        if len(line) >= 3:
            sorted_line = ''.join(sorted(line))
            anagrams[sorted_line][line] += 1
    count = sum((len(value) - 1 for value in anagrams.values()))
    return count >= 86