from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    count = 0
    for group in anagram_dict.values():
        if len(group) >= 2 and all((len(w) >= 3 for w in group)):
            count += len(group) * (len(group) - 1) // 2
    return count <= 52