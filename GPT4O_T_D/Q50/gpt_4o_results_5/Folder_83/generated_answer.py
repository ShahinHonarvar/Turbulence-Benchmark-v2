def if_contains_anagrams(words):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_str(word)
            if sorted_word in anagram_map:
                count += anagram_map[sorted_word]
                anagram_map[sorted_word] += 1
            else:
                anagram_map[sorted_word] = 1
    return count >= 48