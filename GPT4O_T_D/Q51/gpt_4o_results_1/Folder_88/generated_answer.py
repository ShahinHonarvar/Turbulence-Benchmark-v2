def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s))
    normalized_strings = [sorted_string(s.lower()) for s in strings if len(s) >= 3]
    anagram_count = {}
    for s in normalized_strings:
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values() if count > 1))
    return anagram_pairs <= 407