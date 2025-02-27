def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    processed_anagrams = {}
    for s in normalized_strings:
        if s in processed_anagrams:
            processed_anagrams[s] += 1
            anagram_count += processed_anagrams[s] - 1
            if anagram_count >= 30:
                return True
        else:
            processed_anagrams[s] = 1
    return False