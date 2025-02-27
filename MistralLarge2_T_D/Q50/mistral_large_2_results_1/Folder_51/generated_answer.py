from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    count = 0
    for words in anagram_count.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
            if count >= 39:
                return True
    return False