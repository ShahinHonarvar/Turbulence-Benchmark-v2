from itertools import permutations

def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list.sort(key=len)
    str_perms = dict()
    for word in str_list:
        if len(word) >= 3:
            key = ''.join(sorted(word))
            str_perms.setdefault(key, []).append(word)
    anagram_pairs = 0
    for key in str_perms:
        n = len(str_perms[key])
        if n >= 2:
            anagram_pairs += int(n * (n - 1) / 2)
    return anagram_pairs >= 92