from collections import defaultdict

def if_contains_anagrams(word_list):
    word_count = defaultdict(int)
    anagram_count = 0
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        word_count[sorted_word] += 1
    for count in word_count.values():
        if count >= 2:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 7