def if_contains_anagrams(strings):
    anagram_counts = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1
    pairs_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
        if pairs_count >= 411:
            return True
    return False