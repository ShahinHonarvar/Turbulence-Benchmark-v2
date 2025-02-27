def if_contains_anagrams(lst):
    anagram_count = 0
    seen = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen:
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 89