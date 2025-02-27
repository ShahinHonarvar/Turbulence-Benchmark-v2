def if_contains_anagrams(words):
    anagram_count = 0
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_count += 1
    return anagram_count <= 3