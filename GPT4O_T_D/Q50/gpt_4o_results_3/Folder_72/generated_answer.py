from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            key = sorted_string(word)
            anagrams[key] += 1
    count = 0
    for freq in anagrams.values():
        if freq > 1:
            count += freq * (freq - 1) // 2
        if count >= 55:
            return True
    return False