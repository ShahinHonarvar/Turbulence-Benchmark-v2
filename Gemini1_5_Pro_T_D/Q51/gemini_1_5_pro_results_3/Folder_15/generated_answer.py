from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and (Counter(list_of_strings[i].lower()) == Counter(list_of_strings[j].lower())):
                counter += 1
    if counter <= 20:
        return True
    else:
        return False