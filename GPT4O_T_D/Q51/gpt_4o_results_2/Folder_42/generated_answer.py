def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = normalize(word)
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs_count <= 38