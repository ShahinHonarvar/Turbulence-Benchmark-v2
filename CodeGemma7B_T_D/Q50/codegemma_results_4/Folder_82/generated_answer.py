from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_map[sorted_word].append(word)
    count = 0
    for anagrams in str_map.values():
        if len(anagrams) >= 3:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 276