def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    filtered_strings = [s.lower() for s in strings if len(s) >= 3]
    seen = set()
    for i, s1 in enumerate(filtered_strings):
        for s2 in filtered_strings[i + 1:]:
            if s1 not in seen and is_anagram(s1, s2):
                anagram_pairs += 1
                seen.add(s2)
        seen.add(s1)
    return anagram_pairs <= 26