def if_contains_anagrams(words):
    anagram_count = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_count:
            anagram_count[sorted_word] += 1
        else:
            anagram_count[sorted_word] = 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return total_pairs <= 210