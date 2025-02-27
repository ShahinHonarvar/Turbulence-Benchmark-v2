from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_count[normalize(string)] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 209