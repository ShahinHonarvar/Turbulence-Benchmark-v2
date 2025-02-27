import collections

def if_contains_anagrams(word_list):
    anagram_count = 0
    words_seen = set()
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in words_seen:
            continue
        words_seen.add(sorted_word)
        if len(sorted_word) >= 3:
            anagram_count += len(words_seen) - 1
            if anagram_count > 206:
                return False
    return True