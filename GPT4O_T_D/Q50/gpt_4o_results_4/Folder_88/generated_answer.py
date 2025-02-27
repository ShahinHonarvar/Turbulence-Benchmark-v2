from collections import defaultdict

def if_contains_anagrams(string_list):
    pairs_count = 0
    anagram_dict = defaultdict(int)
    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
            if pairs_count >= 34:
                return True
    return False