from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        str_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for anagrams in str_dict.values():
        for i in range(len(anagrams)):
            for j in range(i + 1, len(anagrams)):
                count += 1
                if count >= 41:
                    return True
    return False