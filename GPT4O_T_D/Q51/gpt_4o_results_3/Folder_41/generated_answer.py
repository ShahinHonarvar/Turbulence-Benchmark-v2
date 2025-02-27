from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for word in strings:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize(word)
            anagram_dict[normalized] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs_count <= 52