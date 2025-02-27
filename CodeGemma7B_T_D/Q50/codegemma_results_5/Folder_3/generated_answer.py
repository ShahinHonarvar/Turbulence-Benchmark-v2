from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counts = Counter((str_item for str_item in str_list if len(str_item) >= 3))
    for word_count in anagram_counts.values():
        if word_count >= 30:
            return True
    return False