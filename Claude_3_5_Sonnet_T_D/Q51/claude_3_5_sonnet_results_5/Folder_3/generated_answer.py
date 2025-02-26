from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        word = ''.join(filter(str.isalpha, word.lower()))
        if len(word) < 3 or word in processed:
            continue
        word_counter = Counter(word)
        processed.add(word)
        for other_word in string_list[i + 1:]:
            other_word = ''.join(filter(str.isalpha, other_word.lower()))
            if len(other_word) < 3 or other_word in processed:
                continue
            if Counter(other_word) == word_counter:
                anagram_count += 1
                processed.add(other_word)
                if anagram_count > 66:
                    return False
    return True