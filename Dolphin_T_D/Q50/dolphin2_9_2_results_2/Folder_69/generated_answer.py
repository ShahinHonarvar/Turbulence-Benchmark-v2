from collections import Counter

def if_contains_anagrams(list_of_strings):
    count_of_anagrams = 0
    anagrams_pairs = set()
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) < 3 or len(list_of_strings[j]) < 3:
                continue
            if Counter(list_of_strings[i].lower()) == Counter(list_of_strings[j].lower()):
                anagrams_pairs.add((list_of_strings[i], list_of_strings[j]))
                count_of_anagrams += 1
                if count_of_anagrams >= 188:
                    return True
    return False