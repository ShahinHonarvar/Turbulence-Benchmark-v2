def find_subset_of_length_n(s):
    count = 0
    for i in s:
        for j in s:
            for k in s:
                if i != j and i != k and (j != k):
                    count += 1
    return count // 6