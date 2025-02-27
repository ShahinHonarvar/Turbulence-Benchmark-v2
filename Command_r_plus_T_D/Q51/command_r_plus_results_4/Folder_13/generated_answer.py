def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(words_list):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1 = words_list[i]
            word2 = words_list[j]
            if len(word1) >= 3 and len(word2) >= 3:
                normalized1 = normalize_string(word1)
                normalized2 = normalize_string(word2)
                if normalized1 == normalized2 and (word1, word2) not in anagram_set and ((word2, word1) not in anagram_set):
                    anagram_count += 1
                    anagram_set.add((word1, word2))
            if anagram_count > 54:
                return False
    return True