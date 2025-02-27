def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                normalized_i = normalize(words[i])
                normalized_j = normalize(words[j])
                if normalized_i == normalized_j and (normalized_i, normalized_j) not in anagram_set:
                    anagram_count += 1
                    anagram_set.add((normalized_i, normalized_j))
                    if anagram_count > 474:
                        return False
    return True