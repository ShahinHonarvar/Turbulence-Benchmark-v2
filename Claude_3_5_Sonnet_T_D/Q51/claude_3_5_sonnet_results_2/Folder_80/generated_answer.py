from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word1 in enumerate(string_list):
        if len(word1) < 3:
            continue
        word1 = ''.join(filter(str.isalpha, word1.lower()))
        if word1 in processed:
            continue
        processed.add(word1)
        sorted_word1 = ''.join(sorted(word1))
        for word2 in string_list[i + 1:]:
            if len(word2) < 3:
                continue
            word2 = ''.join(filter(str.isalpha, word2.lower()))
            if word2 in processed:
                continue
            if len(word1) == len(word2) and sorted_word1 == ''.join(sorted(word2)):
                anagram_count += 1
                if anagram_count > 255:
                    return False
    return True