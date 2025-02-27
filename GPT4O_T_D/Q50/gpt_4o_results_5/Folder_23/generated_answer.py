from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for word_list in anagram_dict.values():
        n = len(word_list)
        anagram_count += n * (n - 1) // 2
        if anagram_count >= 67:
            return True
    return False