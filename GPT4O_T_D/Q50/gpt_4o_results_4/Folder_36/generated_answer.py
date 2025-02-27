from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            key = sorted_string(word)
            anagrams[key] += 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs >= 312:
                return True
    return False