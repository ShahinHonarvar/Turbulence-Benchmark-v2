from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(int)
    count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count += anagram_map[sorted_word]
            anagram_map[sorted_word] += 1
            if count >= 66:
                return True
    return False