from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_representation(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(set)
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_representation(word)
            anagram_dict[sorted_word].add(word)
    count = 0
    for anagram_group in anagram_dict.values():
        n = len(anagram_group)
        count += n * (n - 1) // 2
        if count > 474:
            return False
    return True