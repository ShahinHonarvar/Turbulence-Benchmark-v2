from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_key(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            key = sorted_key(word)
            anagram_dict[key] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 98