from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values() if len(group) > 1))
    return count <= 60