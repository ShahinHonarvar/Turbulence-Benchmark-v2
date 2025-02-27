def if_contains_anagrams(strings):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in strings:
        if len(word) >= 3:
            form = canonical_form(word)
            if form in anagram_counts:
                anagram_counts[form] += 1
            else:
                anagram_counts[form] = 1
    total_pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs > 475:
            return False
    return True