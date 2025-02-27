from collections import Counter

def if_contains_anagrams(s):
    count = 0
    counter_list = []
    for word in s:
        counter_list.append(Counter(word.lower()))
    for i in range(len(counter_list) - 1):
        for j in range(i + 1, len(counter_list)):
            if len(counter_list[i]) >= 3 and len(counter_list[j]) >= 3 and (counter_list[i] == counter_list[j]):
                count += 1
    if count > 17:
        return False
    else:
        return True