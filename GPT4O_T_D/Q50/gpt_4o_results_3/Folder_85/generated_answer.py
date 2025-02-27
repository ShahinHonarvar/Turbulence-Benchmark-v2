from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count += anagram_dict[sorted_word]
            anagram_dict[sorted_word] += 1
    return count >= 73