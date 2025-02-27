def if_contains_anagrams(words):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = sorted_chars(word)
        if sorted_word in anagram_counts:
            anagram_counts[sorted_word] += 1
        else:
            anagram_counts[sorted_word] = 1
    num_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return num_pairs >= 10