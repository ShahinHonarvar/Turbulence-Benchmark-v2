def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = 0
    normalized_words = [normalize(s) for s in strings if len(s) >= 3]
    anagram_count = {}
    for word in normalized_words:
        if word in anagram_count:
            anagram_count[word] += 1
        else:
            anagram_count[word] = 1
    for value in anagram_count.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 136