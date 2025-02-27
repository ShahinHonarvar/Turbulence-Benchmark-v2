from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_map[normalized] += 1
    count = 0
    for frequency in anagram_map.values():
        if frequency > 1:
            count += frequency * (frequency - 1) // 2
        if count >= 177:
            return True
    return False