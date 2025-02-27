def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize(word) for word in words if len(word) >= 3]
    anagram_pairs = 0
    counted_pairs = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j]:
                pair = tuple(sorted((words[i].lower(), words[j].lower())))
                if pair not in counted_pairs:
                    anagram_pairs += 1
                    counted_pairs.add(pair)
                if anagram_pairs > 78:
                    return False
    return True