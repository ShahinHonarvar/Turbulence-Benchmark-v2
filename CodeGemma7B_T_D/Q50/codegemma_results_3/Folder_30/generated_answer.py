from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for str in str_list:
        str_dict[''.join(sorted(str.lower()))].append(str)
    pairs = 0
    for anagrams in str_dict.values():
        for i in range(len(anagrams)):
            for j in range(i + 1, len(anagrams)):
                if len(anagrams[i]) >= 3 and len(anagrams[j]) >= 3:
                    pairs += 1
    return pairs >= 78