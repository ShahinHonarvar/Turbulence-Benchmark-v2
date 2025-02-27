def if_contains_anagrams(lst):
    anagram_count = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagram_count:
                anagram_count[sorted_word] += 1
            else:
                anagram_count[sorted_word] = 1
    anagram_pairs = sum([count * (count - 1) // 2 for count in anagram_count.values()])
    return anagram_pairs >= 106