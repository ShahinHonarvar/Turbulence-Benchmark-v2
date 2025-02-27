from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_count = defaultdict(int)
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    return sum((count >= 2 for count in anagram_count.values())) >= 2