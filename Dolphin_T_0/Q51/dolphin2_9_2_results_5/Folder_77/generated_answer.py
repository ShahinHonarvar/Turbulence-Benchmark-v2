import itertools

def if_contains_anagrams(lst):
    count = 0
    for pair in itertools.combinations(lst, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3:
            if sorted(pair[0].lower()) == sorted(pair[1].lower()):
                count += 1
    return count <= 17