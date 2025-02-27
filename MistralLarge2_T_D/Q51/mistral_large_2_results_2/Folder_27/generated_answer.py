from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_dict[normalized].append(word)
    count = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 113