import collections

def if_contains_anagrams(words):
    count = 0
    d = collections.defaultdict(set)
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            d[key].add(word)
    for key in d:
        n = len(d[key])
        count += n * (n - 1) // 2
    return count <= 54