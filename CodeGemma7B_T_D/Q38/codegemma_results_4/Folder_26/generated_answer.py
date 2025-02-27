def find_subset_of_length_n(a_set):
    result = 0
    for i in range(len(a_set)):
        for j in range(i + 1, len(a_set)):
            for k in range(j + 1, len(a_set)):
                if len({a_set[i], a_set[j], a_set[k]}) == 3:
                    result += 1
    return result