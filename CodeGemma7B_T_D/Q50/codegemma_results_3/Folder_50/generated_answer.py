from collections import defaultdict

def if_contains_anagrams(word_list):
    anagrams = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) >= 3:
            count += len(group) * (len(group) - 1) // 2
    return count >= 20