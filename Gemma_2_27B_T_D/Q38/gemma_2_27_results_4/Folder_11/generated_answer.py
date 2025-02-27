def find_subset_of_length_n(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                for l in range(k + 1, len(data)):
                    for m in range(l + 1, len(data)):
                        for n in range(m + 1, len(data)):
                            for o in range(n + 1, len(data)):
                                for p in range(o + 1, len(data)):
                                    subset = {data[i], data[j], data[k], data[l], data[m], data[n], data[o], data[p]}
                                    if len(subset) == 77:
                                        count += 1
    return count