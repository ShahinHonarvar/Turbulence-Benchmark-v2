from collections import Counter

def if_contains_anagrams(lst_strings):
    count = 0
    for i in range(len(lst_strings)):
        for j in range(i + 1, len(lst_strings)):
            if len(lst_strings[i]) >= 3 and len(lst_strings[j]) >= 3:
                count += Counter(lst_strings[i].lower()) == Counter(lst_strings[j].lower())
    return count <= 276