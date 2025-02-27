def if_contains_anagrams(lst):
    anagram_count = 0
    normalized_groups = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in normalized_groups:
                normalized_groups[sorted_word] += 1
            else:
                normalized_groups[sorted_word] = 1
    for count in normalized_groups.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 65:
            return True
    return False