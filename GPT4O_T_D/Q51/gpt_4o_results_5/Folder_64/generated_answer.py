from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if anagram_dict[normalized_word] > 0:
                anagram_count += anagram_dict[normalized_word]
            anagram_dict[normalized_word] += 1
        if anagram_count > 59:
            return False
    return True