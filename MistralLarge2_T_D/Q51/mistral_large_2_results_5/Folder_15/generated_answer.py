from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            form = canonical_form(word)
            anagram_dict[form].append(word)
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
            if anagram_pairs > 20:
                return False
    return anagram_pairs <= 20