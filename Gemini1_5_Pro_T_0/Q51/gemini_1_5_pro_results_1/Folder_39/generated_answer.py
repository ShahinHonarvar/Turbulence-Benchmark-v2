import itertools

def if_contains_anagrams(list_of_strings):
    pairs = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and (len(list_of_strings[i]) == len(list_of_strings[j])):
                if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    pairs += 1
    if pairs <= 257:
        return True
    else:
        return False