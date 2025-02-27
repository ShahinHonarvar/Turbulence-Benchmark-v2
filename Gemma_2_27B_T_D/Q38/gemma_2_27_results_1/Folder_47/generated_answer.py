def find_subset_of_length_n(data):
    n = 34
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if len({data[i], data[j], data[k]}) == n:
                    count += 1
    return count