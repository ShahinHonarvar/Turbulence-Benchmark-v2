import collections

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        anagrams.append(sorted_word)
    count = collections.defaultdict(int)
    for word in anagrams:
        count[word] += 1
    return sum(count.values()) <= 74