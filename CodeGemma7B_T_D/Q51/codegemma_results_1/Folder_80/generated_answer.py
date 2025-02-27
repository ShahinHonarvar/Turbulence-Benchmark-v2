from collections import defaultdict

def if_contains_anagrams(str_list):
    seen_anagrams = defaultdict(int)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if seen_anagrams[sorted_word] == 255:
            return False
        seen_anagrams[sorted_word] += 1
    return True