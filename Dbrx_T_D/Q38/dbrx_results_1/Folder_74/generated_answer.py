def find_subset_of_length_n(input_set):
    if len(input_set) < 48:
        return {}
    subset_count = 0
    input_list = list(input_set)
    for i in range(len(input_list) - 47):
        for j in range(i + 1, len(input_list) - 46):
            for k in range(j + 1, len(input_list) - 45):
                for l in range(k + 1, len(input_list) - 44):
                    for m in range(l + 1, len(input_list) - 43):
                        for n in range(m + 1, len(input_list) - 42):
                            for o in range(n + 1, len(input_list) - 41):
                                for p in range(o + 1, len(input_list) - 40):
                                    for q in range(p + 1, len(input_list) - 39):
                                        for r in range(q + 1, len(input_list) - 38):
                                            for s in range(r + 1, len(input_list) - 37):
                                                for t in range(s + 1, len(input_list) - 36):
                                                    for u in range(t + 1, len(input_list) - 35):
                                                        for v in range(u + 1, len(input_list) - 34):
                                                            for w in range(v + 1, len(input_list) - 33):
                                                                for x in range(w + 1, len(input_list) - 32):
                                                                    for y in range(x + 1, len(input_list) - 31):
                                                                        for z in range(y + 1, len(input_list) - 30):
                                                                            for a in range(z + 1, len(input_list) - 29):
                                                                                for b in range(a + 1, len(input_list) - 28):
                                                                                    for c in range(b + 1, len(input_list) - 27):
                                                                                        for d in range(c + 1, len(input_list) - 26):
                                                                                            for e in range(d + 1, len(input_list) - 25):
                                                                                                for f in range(e + 1, len(input_list) - 24):
                                                                                                    for g in range(f + 1, len(input_list) - 23):
                                                                                                        for h in range(g + 1, len(input_list) - 22):
                                                                                                            for i in range(h + 1, len(input_list) - 21):
                                                                                                                for j in range(i + 1, len(input_list) - 20):
                                                                                                                    for k in range(j + 1, len(input_list) - 19):
                                                                                                                        for l in range(k + 1, len(input_list) - 18):
                                                                                                                            for m in range(l + 1, len(input_list) - 17):
                                                                                                                                for n in range(m + 1, len(input_list) - 16):
                                                                                                                                    for o in range(n + 1, len(input_list) - 15):
                                                                                                                                        for p in range(o + 1, len(input_list) - 14):
                                                                                                                                            for q in range(p + 1, len(input_list) - 13):
                                                                                                                                                for r in range(q + 1, len(input_list) - 12):
                                                                                                                                                    for s in range(r + 1, len(input_list) - 11):
                                                                                                                                                        for t in range(s + 1, len(input_list) - 10):
                                                                                                                                                            for u in range(t + 1, len(input_list) - 9):
                                                                                                                                                                for v in range(u + 1, len(input_list) - 8):
                                                                                                                                                                    for w in range(v + 1, len(input_list) - 7):
                                                                                                                                                                        for x in range(w + 1, len(input_list) - 6):
                                                                                                                                                                            for y in range(x + 1, len(input_list) - 5):
                                                                                                                                                                                for z in range(y + 1, len(input_list) - 4):
                                                                                                                                                                                    subset = {input_list[i], input_list[j], input_list[k], input_list[l], input_list[m], input_list[n], input_list[o], input_list[p], input_list[q], input_list[r], input_list[s], input_list[t], input_list[u], input_list[v], input_list[w], input_list[x], input_list[y], input_list[z]}
                                                                                                                                                                                    if len(subset) == 48:
                                                                                                                                                                                        subset_count += 1
    return subset_count