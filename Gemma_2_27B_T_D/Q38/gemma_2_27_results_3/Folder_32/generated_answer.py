def find_subset_of_length_n(elements):
    n = 22
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for o in range(m + 1, len(elements)):
                            for p in range(o + 1, len(elements)):
                                for q in range(p + 1, len(elements)):
                                    for r in range(q + 1, len(elements)):
                                        for s in range(r + 1, len(elements)):
                                            for t in range(s + 1, len(elements)):
                                                for u in range(t + 1, len(elements)):
                                                    for v in range(u + 1, len(elements)):
                                                        for w in range(v + 1, len(elements)):
                                                            for x in range(w + 1, len(elements)):
                                                                for y in range(x + 1, len(elements)):
                                                                    for z in range(y + 1, len(elements)):
                                                                        count += 1
    return count