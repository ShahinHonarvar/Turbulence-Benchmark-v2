def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = sort_string(word)
            if sorted_word in anagram_count:
                anagram_count[sorted_word] += 1
            else:
                anagram_count[sorted_word] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 22