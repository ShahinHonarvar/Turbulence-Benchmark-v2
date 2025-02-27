from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagram_dict:
                anagram_count += 1
                if anagram_count > 69:
                    return False
            else:
                anagram_dict[sorted_word] = Counter(word_lower)
    return True