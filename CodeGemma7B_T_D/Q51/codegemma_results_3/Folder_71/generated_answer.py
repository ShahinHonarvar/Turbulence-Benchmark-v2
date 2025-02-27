def if_contains_anagrams(list):
    pairs = 0
    for word in list:
        for other in list[list.index(word) + 1:]:
            if sorted([i.lower() for i in word]) == sorted([j.lower() for j in other]):
                pairs += 1
    return pairs <= 9