from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_of_anagrams <= 41