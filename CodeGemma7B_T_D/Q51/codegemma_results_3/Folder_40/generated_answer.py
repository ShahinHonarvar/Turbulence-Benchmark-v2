from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        str1 = ''.join(sorted(str1.lower()))
        str2 = ''.join(sorted(str2.lower()))
        return str1 == str2
    hash_map = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        hash_map[key].append(string)
    pairs = 0
    for anagrams in hash_map.values():
        if len(anagrams) > 2:
            pairs += len(anagrams) * (len(anagrams) - 1) // 2
        else:
            pairs += 0
    return pairs <= 29