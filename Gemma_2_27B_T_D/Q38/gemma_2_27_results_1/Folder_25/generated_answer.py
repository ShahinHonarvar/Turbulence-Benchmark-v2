def find_subset_of_length_n(items):
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            for k in range(j + 1, len(items)):
                for l in range(k + 1, len(items)):
                    for m in range(l + 1, len(items)):
                        for n in range(m + 1, len(items)):
                            for o in range(n + 1, len(items)):
                                for p in range(o + 1, len(items)):
                                    for q in range(p + 1, len(items)):
                                        for r in range(q + 1, len(items)):
                                            for s in range(r + 1, len(items)):
                                                for t in range(s + 1, len(items)):
                                                    if len({items[i], items[j], items[k], items[l], items[m], items[n], items[o], items[p], items[q], items[r], items[s], items[t]}) == 90:
                                                        count += 1
    return count