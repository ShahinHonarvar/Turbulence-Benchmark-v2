def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and are_anagrams(words[i], words[j]):
                valid_anagram_pairs += 1
                if valid_anagram_pairs > 93:
                    return False
    return True