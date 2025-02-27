from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(int)
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[word] += 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 67