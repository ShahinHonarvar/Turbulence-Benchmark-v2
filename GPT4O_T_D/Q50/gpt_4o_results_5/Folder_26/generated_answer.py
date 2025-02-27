from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 49:
            return True
    return False