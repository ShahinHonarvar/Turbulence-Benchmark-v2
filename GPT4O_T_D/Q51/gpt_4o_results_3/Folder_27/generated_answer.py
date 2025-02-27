def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    seen = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized_word = normalize(word)
        if normalized_word in seen:
            anagram_pairs += seen[normalized_word]
            seen[normalized_word] += 1
        else:
            seen[normalized_word] = 1
    return anagram_pairs <= 113