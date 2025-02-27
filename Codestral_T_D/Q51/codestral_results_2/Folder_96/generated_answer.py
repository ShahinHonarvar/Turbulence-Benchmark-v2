def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    anagram_pairs = [group for group in anagrams.values() if len(group) > 1]
    return len(anagram_pairs) <= 2