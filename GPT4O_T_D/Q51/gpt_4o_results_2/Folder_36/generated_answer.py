def if_contains_anagrams(lst):

    def get_sorted_string(s):
        return ''.join(sorted(s.lower()))
    potential_anagrams = [word for word in lst if len(word) >= 3]
    anagram_counts = {}
    for word in potential_anagrams:
        sorted_word = get_sorted_string(word)
        if sorted_word in anagram_counts:
            anagram_counts[sorted_word] += 1
        else:
            anagram_counts[sorted_word] = 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 25