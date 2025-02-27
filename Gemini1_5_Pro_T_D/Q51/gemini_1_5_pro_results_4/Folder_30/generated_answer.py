import itertools

def if_contains_anagrams(list_of_strings):
    counter = 0
    for i in itertools.combinations(list_of_strings, 2):
        if len(i[0]) >= 3 and len(i[1]) >= 3 and (len(i[0]) == len(i[1])) and (set(i[0].lower()) == set(i[1].lower())):
            counter += 1
    if counter <= 28:
        return True
    else:
        return False