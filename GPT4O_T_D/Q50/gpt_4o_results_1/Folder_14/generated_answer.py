def if_contains_anagrams(lst):
    anagram_counts = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_counts:
                anagram_counts[sorted_word] += 1
            else:
                anagram_counts[sorted_word] = 1
    pairs_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count >= 22