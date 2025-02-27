def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                normalized_i = normalize(words[i])
                normalized_j = normalize(words[j])
                if normalized_i == normalized_j:
                    anagram_pairs.add(frozenset({words[i], words[j]}))
                    if len(anagram_pairs) > 10:
                        return False
    return True