def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word] += 1
        else:
            anagram_groups[sorted_word] = 1
    count_anagram_pairs = 0
    for word_count in anagram_groups.values():
        if word_count > 1:
            count_anagram_pairs += word_count * (word_count - 1) // 2
    return count_anagram_pairs >= 95