from collections import defaultdict

def if_contains_anagrams(words):

    def is_valid_anagram_pair(w1, w2):
        return sorted(w1) == sorted(w2) and (len(w1) >= 3 and len(w2) >= 3)
    count = 0
    seen = defaultdict(set)
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in seen:
            for s in seen[sorted_word]:
                if is_valid_anagram_pair(word_lower, s):
                    count += 1
                    if count > 81:
                        return False
        seen[sorted_word].add(word_lower)
    return True