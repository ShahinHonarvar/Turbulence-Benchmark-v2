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
                                    for q in range(p + 1, len(data)):
                                        for r in range(q + 1, len(data)):
                                            for s in range(r + 1, len(data)):
                                                for t in range(s + 1, len(data)):
                                                    if len({data[i], data[j], data[k], data[l], data[m], data[n], data[o], data[p], data[q], data[r], data[s], data[t]}) == 100:
                                                        count += 1
    return count