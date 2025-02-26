from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        if word in processed or len(word) < 3:
            continue
        word = ''.join(filter(str.isalpha, word.lower()))
        if len(word) < 3:
            continue
        word_counter = Counter(word)
        for j in range(i + 1, len(string_list)):
            other_word = string_list[j]
            if other_word in processed or len(other_word) < 3:
                continue
            other_word = ''.join(filter(str.isalpha, other_word.lower()))
            if len(other_word) < 3:
                continue
            if Counter(other_word) == word_counter:
                anagram_count += 1
                processed.add(string_list[i])
                processed.add(string_list[j])
                if anagram_count > 3:
                    return False
                break
    return True