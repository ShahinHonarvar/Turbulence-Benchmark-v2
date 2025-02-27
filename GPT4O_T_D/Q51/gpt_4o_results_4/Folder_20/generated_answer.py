from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    stripped_words = [''.join(filter(str.isalpha, word)).lower() for word in words if len(word) >= 3]
    anagram_dict = defaultdict(int)
    for word in stripped_words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count > 131:
            return False
    return True