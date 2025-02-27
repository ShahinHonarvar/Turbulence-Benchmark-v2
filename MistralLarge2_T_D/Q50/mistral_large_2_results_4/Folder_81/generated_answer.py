from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1 and len(key) >= 3:
            anagram_count += len(anagram_dict[key]) - 1
            if anagram_count >= 16:
                return True
    return False