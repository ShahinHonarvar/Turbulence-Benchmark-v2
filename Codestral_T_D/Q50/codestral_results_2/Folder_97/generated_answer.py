def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = [word]
            else:
                anagram_groups[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs >= 123