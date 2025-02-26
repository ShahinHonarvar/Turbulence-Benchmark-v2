from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_words = set()
    for word in string_list:
        word = ''.join(filter(str.isalpha, word.lower()))
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in processed_words:
            processed_words.add(sorted_word)
        else:
            anagram_count += 1
            if anagram_count > 75:
                return False
    return True