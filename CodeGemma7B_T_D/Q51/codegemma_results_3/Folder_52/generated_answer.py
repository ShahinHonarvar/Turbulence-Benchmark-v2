def if_contains_anagrams(lst):
    list_of_tuples = []
    count = 0
    for i in lst:
        if len(i) >= 3:
            tuple_i = tuple(sorted(i.lower()))
            list_of_tuples.append(tuple_i)
    for i in range(len(list_of_tuples)):
        for j in range(i + 1, len(list_of_tuples)):
            if list_of_tuples[i] == list_of_tuples[j]:
                count += 1
                if count > 43:
                    return False
    return True