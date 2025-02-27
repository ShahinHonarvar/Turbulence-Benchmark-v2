def if_contains_anagrams(strings):
    anagram_counts = {}
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_counts:
            anagram_counts[sorted_word] += 1
        else:
            anagram_counts[sorted_word] = 1
    pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 116:
                return False
    return True