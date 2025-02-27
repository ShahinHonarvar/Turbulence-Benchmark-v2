import collections

def if_contains_anagrams(words):
    anagrams = collections.defaultdict(list)
    for word in words:
        sorted_word = tuple(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for word_list in anagrams.values():
        count += len(word_list) * (len(word_list) - 1) // 2
        if count > 255 * 254 // 2:
            return True
    return False