from collections import defaultdict
        import re

def if_contains_anagrams(str_list):
    dict = defaultdict(lambda: defaultdict(int))
    for word in str_list:
        temp_word = re.sub('[^a-zA-Z]', '', word).lower()
        if len(temp_word) >= 3:
            dict[len(word)][temp_word] += 1
    count = 0
    for k in dict.keys():
        for i in dict[k].values():
            if i > 1:
                count += i * (i - 1) // 2
    return count >= 155