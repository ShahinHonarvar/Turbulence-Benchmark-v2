from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                if Counter(list_of_strings[i].lower()) == Counter(list_of_strings[j].lower()):
                    count += 1
                    if count >= 89:
                        return True
    return count <= 89