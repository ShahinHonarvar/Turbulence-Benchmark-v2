from collections import Counter

def if_contains_anagrams(lst):
    counter_list = [Counter(i.lower()) for i in lst if len(i) >= 3]
    count = 0
    for i in range(len(counter_list)):
        for j in range(i + 1, len(counter_list)):
            if counter_list[i] == counter_list[j]:
                count += 1
    return count >= 219