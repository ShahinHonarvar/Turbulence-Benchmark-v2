from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i]) < 3:
            continue
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[j]) < 3:
                continue
            counter1 = Counter(list_of_strings[i].lower())
            counter2 = Counter(list_of_strings[j].lower())
            if counter1 == counter2:
                count += 1
    if count > 181:
        return False
    else:
        return True