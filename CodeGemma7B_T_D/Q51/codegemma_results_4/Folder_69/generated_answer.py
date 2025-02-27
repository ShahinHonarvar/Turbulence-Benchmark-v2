from collections import defaultdict

def if_contains_anagrams(str_list):
    char_count = defaultdict(int)
    for word in str_list:
        word = ''.join((ch.lower() for ch in word if ch.isalpha()))
        if len(word) < 3:
            continue
        for char in word:
            char_count[char] += 1
    anagram_count = 0
    for count in char_count.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 58