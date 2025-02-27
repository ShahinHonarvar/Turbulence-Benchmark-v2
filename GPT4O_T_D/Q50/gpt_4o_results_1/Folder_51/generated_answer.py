def if_contains_anagrams(strings):
    anagram_count = 0
    seen = {}
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen:
            anagram_count += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    return anagram_count >= 39