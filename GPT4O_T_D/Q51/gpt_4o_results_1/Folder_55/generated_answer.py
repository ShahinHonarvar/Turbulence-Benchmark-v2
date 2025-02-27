def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize(word) for word in words if len(word) >= 3]
    count = 0
    seen = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and (i, j) not in seen:
                count += 1
                seen.add((i, j))
    return count <= 44