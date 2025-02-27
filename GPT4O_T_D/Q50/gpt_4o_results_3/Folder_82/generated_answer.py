def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    counted_anagrams = {}
    for word in normalized_strings:
        if word in counted_anagrams:
            counted_anagrams[word] += 1
        else:
            counted_anagrams[word] = 1
    for count in counted_anagrams.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 276