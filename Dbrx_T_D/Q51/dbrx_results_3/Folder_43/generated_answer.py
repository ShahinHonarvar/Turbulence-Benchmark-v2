import collections

def if_contains_anagrams(words):
    anagrams = collections.defaultdict(lambda: [])
    for word in words:
        if len(word) < 3:
            continue
        anagrams[''.join(sorted(word.lower()))].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += 1
    return count <= 3