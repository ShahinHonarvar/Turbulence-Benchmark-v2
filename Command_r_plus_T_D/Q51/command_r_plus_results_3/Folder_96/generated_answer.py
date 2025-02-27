def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_count:
            anagram_count[sorted_word] += 1
        else:
            anagram_count[sorted_word] = 1
    anagram_pairs = [count for count in anagram_count.values() if count > 1]
    return len(anagram_pairs) <= 2