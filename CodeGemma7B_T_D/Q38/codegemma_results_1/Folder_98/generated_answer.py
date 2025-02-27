def find_subset_of_length_n(a):
    count = 0
    for i in a:
        for j in a:
            for k in a:
                for l in a:
                    if i != j and j != k and (k != l):
                        count += 1
    return count