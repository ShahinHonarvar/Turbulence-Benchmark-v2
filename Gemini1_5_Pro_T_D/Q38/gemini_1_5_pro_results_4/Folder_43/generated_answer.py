def find_subset_of_length_n(set_of_elements):
    n = 29
    if len(set_of_elements) < n:
        return 0
    if len(set_of_elements) == n:
        return 1
    count = 0
    for i in range(len(set_of_elements)):
        for j in range(i + 1, len(set_of_elements)):
            for k in range(j + 1, len(set_of_elements)):
                for l in range(k + 1, len(set_of_elements)):
                    for m in range(l + 1, len(set_of_elements)):
                        for o in range(m + 1, len(set_of_elements)):
                            for p in range(o + 1, len(set_of_elements)):
                                for q in range(p + 1, len(set_of_elements)):
                                    for r in range(q + 1, len(set_of_elements)):
                                        for s in range(r + 1, len(set_of_elements)):
                                            for t in range(s + 1, len(set_of_elements)):
                                                for u in range(t + 1, len(set_of_elements)):
                                                    for v in range(u + 1, len(set_of_elements)):
                                                        for w in range(v + 1, len(set_of_elements)):
                                                            for x in range(w + 1, len(set_of_elements)):
                                                                for y in range(x + 1, len(set_of_elements)):
                                                                    for z in range(y + 1, len(set_of_elements)):
                                                                        for a in range(z + 1, len(set_of_elements)):
                                                                            for b in range(a + 1, len(set_of_elements)):
                                                                                for c in range(b + 1, len(set_of_elements)):
                                                                                    for d in range(c + 1, len(set_of_elements)):
                                                                                        for e in range(d + 1, len(set_of_elements)):
                                                                                            for f in range(e + 1, len(set_of_elements)):
                                                                                                for g in range(f + 1, len(set_of_elements)):
                                                                                                    for h in range(g + 1, len(set_of_elements)):
                                                                                                        count += 1
    return count