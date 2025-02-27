def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(words_list):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word_i = words_list[i]
            word_j = words_list[j]
            if len(word_i) < 3 or len(word_j) < 3:
                continue
            normalized_i = normalize_string(word_i)
            normalized_j = normalize_string(word_j)
            if normalized_i == normalized_j and (word_i, word_j) not in anagram_set:
                anagram_count += 1
                anagram_set.add((word_i, word_j))
                if anagram_count > 21:
                    return False
    return True