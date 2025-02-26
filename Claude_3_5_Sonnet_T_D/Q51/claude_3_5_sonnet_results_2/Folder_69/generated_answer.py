from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        if len(word) < 3:
            continue
        word = ''.join(filter(str.isalpha, word.lower()))
        if word in processed:
            continue
        word_counter = Counter(word)
        for j in range(i + 1, len(string_list)):
            compare_word = string_list[j]
            if len(compare_word) < 3:
                continue
            compare_word = ''.join(filter(str.isalpha, compare_word.lower()))
            if compare_word in processed:
                continue
            if len(word) == len(compare_word) and Counter(compare_word) == word_counter:
                anagram_count += 1
                processed.add(word)
                processed.add(compare_word)
                if anagram_count > 58:
                    return False
                break
    return True