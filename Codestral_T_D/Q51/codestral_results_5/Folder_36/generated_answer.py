from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    count = 0
    for anagram_list in anagrams.values():
        n = len(anagram_list)
        count += n * (n - 1) // 2
        if count > 25:
            return False
    return True