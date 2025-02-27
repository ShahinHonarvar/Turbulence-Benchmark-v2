from collections import Counter

def if_contains_anagrams(list_of_strings):
    pair_counter = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                string_1 = Counter(list_of_strings[i].lower())
                string_2 = Counter(list_of_strings[j].lower())
                if string_1 == string_2:
                    pair_counter += 1
                    if pair_counter > 4:
                        return True
    return pair_counter <= 4