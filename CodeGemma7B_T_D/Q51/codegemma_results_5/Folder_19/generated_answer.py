from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    pair_count = 0
    for group in anagrams.values():
        if len(group) > 1:
            pair_count += len(group) * (len(group) - 1) // 2
    return pair_count <= 69