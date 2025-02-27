def find_subset_of_length_n(input_set):
    count = 0
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                for l in range(k + 1, len(input_set)):
                    for m in range(l + 1, len(input_set)):
                        for n in range(m + 1, len(input_set)):
                            for o in range(n + 1, len(input_set)):
                                for p in range(o + 1, len(input_set)):
                                    for q in range(p + 1, len(input_set)):
                                        for r in range(q + 1, len(input_set)):
                                            for s in range(r + 1, len(input_set)):
                                                for t in range(s + 1, len(input_set)):
                                                    for u in range(t + 1, len(input_set)):
                                                        for v in range(u + 1, len(input_set)):
                                                            for w in range(v + 1, len(input_set)):
                                                                for x in range(w + 1, len(input_set)):
                                                                    for y in range(x + 1, len(input_set)):
                                                                        for z in range(y + 1, len(input_set)):
                                                                            count += 1
    return count