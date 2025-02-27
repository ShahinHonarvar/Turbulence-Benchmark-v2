from collections import defaultdict

def if_contains_anagrams(words):
    count_dict = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        count_dict[sorted_word] += 1
    pair_count = sum((v * (v - 1) // 2 for v in count_dict.values()))
    return pair_count <= 279