from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    word_dict = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_dict[sorted_word] += 1
    for count in word_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count >= 47:
            return True
    return False