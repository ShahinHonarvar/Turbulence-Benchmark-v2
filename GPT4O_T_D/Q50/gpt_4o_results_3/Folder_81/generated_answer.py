from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    words_lower = [word.lower() for word in words if len(word) >= 3]
    anagrams_dict = defaultdict(list)
    for word in words_lower:
        sorted_word = ''.join(sorted(word))
        anagrams_dict[sorted_word].append(word)
    anagram_pairs_count = 0
    for anagram_list in anagrams_dict.values():
        count = len(anagram_list)
        if count > 1:
            anagram_pairs_count += count * (count - 1) // 2
    return anagram_pairs_count >= 16