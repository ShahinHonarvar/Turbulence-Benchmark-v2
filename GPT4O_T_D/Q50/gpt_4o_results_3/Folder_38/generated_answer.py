from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_dict[normalized_word].append(word)
    count = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 24:
            return True
    return False