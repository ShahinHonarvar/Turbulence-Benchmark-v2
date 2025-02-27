from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter_dict = {}
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                str_i = Counter(list_of_strings[i].lower())
                str_j = Counter(list_of_strings[j].lower())
                if str_i == str_j:
                    counter_dict[list_of_strings[i]] = list_of_strings[j]
    if len(counter_dict) > 8:
        return False
    else:
        return True