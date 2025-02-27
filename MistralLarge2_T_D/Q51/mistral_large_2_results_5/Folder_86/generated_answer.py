from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_dict = defaultdict(list)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams_dict[sorted_word].append(word)
    anagram_count = sum((len(group) // 2 for group in anagrams_dict.values() if len(group) > 1))
    return anagram_count <= 48