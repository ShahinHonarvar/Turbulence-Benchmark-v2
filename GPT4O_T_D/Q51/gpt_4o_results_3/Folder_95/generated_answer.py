def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    normalized_words = [word.lower() for word in words]
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3 and ((i, j) not in checked_pairs) and ((j, i) not in checked_pairs):
                if is_anagram(normalized_words[i], normalized_words[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 6:
                        return False
                checked_pairs.add((i, j))
    return True