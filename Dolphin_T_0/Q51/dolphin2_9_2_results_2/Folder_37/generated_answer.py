from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for i in range(len(lst)):
        counter = Counter(lst[i].lower())
        key = ''.join(sorted(lst[i].lower()))
        if len(counter) >= 3:
            if key not in anagram_dict:
                anagram_dict[key] = [i]
            else:
                anagram_dict[key].append(i)
    count = 0
    keys = list(anagram_dict.keys())
    for i in range(len(keys)):
        if len(anagram_dict[keys[i]]) > 1:
            count += len(anagram_dict[keys[i]]) * (len(anagram_dict[keys[i]]) - 1) // 2
    return count <= 206