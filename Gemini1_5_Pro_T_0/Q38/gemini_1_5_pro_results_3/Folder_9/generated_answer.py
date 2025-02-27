def find_subset_of_length_n(set_of_elements):
    n = 24
    number_of_subsets = 0
    if len(set_of_elements) >= n:
        for i in range(len(set_of_elements) - n + 1):
            for j in range(i + 1, len(set_of_elements) - n + 2):
                for k in range(j + 1, len(set_of_elements) - n + 3):
                    for l in range(k + 1, len(set_of_elements) - n + 4):
                        for m in range(l + 1, len(set_of_elements) - n + 5):
                            for n in range(m + 1, len(set_of_elements) - n + 6):
                                for o in range(n + 1, len(set_of_elements) - n + 7):
                                    for p in range(o + 1, len(set_of_elements) - n + 8):
                                        for q in range(p + 1, len(set_of_elements) - n + 9):
                                            for r in range(q + 1, len(set_of_elements) - n + 10):
                                                for s in range(r + 1, len(set_of_elements) - n + 11):
                                                    for t in range(s + 1, len(set_of_elements) - n + 12):
                                                        for u in range(t + 1, len(set_of_elements) - n + 13):
                                                            for v in range(u + 1, len(set_of_elements) - n + 14):
                                                                for w in range(v + 1, len(set_of_elements) - n + 15):
                                                                    for x in range(w + 1, len(set_of_elements) - n + 16):
                                                                        for y in range(x + 1, len(set_of_elements) - n + 17):
                                                                            for z in range(y + 1, len(set_of_elements) - n + 18):
                                                                                for a in range(z + 1, len(set_of_elements) - n + 19):
                                                                                    for b in range(a + 1, len(set_of_elements) - n + 20):
                                                                                        for c in range(b + 1, len(set_of_elements) - n + 21):
                                                                                            for d in range(c + 1, len(set_of_elements) - n + 22):
                                                                                                for e in range(d + 1, len(set_of_elements) - n + 23):
                                                                                                    for f in range(e + 1, len(set_of_elements) - n + 24):
                                                                                                        number_of_subsets += 1
    return number_of_subsets