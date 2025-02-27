def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize(word) for word in words]
    anagram_pairs = []
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and len(words[i]) >= 3 and (len(words[j]) >= 3):
                anagram_pairs.append((words[i], words[j]))
    return len(anagram_pairs) <= 2