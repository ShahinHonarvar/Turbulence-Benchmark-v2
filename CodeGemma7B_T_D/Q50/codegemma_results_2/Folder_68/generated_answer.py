from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 9:
            count += 1
    return count >= 9