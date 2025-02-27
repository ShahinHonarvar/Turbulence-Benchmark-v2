from collections import Counter

def if_contains_anagrams(list_of_strings):
    pairs_of_anagrams = 0
    for i in range(0, len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and (Counter(list_of_strings[i].lower()) == Counter(list_of_strings[j].lower())):
                pairs_of_anagrams += 1
    if pairs_of_anagrams <= 96:
        return True
    else:
        return False