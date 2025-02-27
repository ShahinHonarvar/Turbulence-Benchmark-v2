def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    word_map = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in word_map:
            anagram_pairs.add(frozenset({word, word_map[normalized]}))
        else:
            word_map[normalized] = word
    return len(anagram_pairs) <= 91