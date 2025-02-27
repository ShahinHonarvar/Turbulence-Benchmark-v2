def all_substring_of_size_n(str):
    str_list = list(str)
    ok_list = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            for k in range(j + 1, len(str_list)):
                for l in range(k + 1, len(str_list)):
                    for m in range(l + 1, len(str_list)):
                        for n in range(m + 1, len(str_list)):
                            for o in range(n + 1, len(str_list)):
                                for p in range(o + 1, len(str_list)):
                                    for q in range(p + 1, len(str_list)):
                                        for r in range(q + 1, len(str_list)):
                                            for s in range(r + 1, len(str_list)):
                                                for t in range(s + 1, len(str_list)):
                                                    for u in range(t + 1, len(str_list)):
                                                        for v in range(u + 1, len(str_list)):
                                                            for w in range(v + 1, len(str_list)):
                                                                for x in range(w + 1, len(str_list)):
                                                                    for y in range(x + 1, len(str_list)):
                                                                        for z in range(y + 1, len(str_list)):
                                                                            for a in range(z + 1, len(str_list)):
                                                                                for b in range(a + 1, len(str_list)):
                                                                                    for c in range(b + 1, len(str_list)):
                                                                                        for d in range(c + 1, len(str_list)):
                                                                                            for e in range(d + 1, len(str_list)):
                                                                                                for f in range(e + 1, len(str_list)):
                                                                                                    for g in range(f + 1, len(str_list)):
                                                                                                        for h in range(g + 1, len(str_list)):
                                                                                                            for i in range(h + 1, len(str_list)):
                                                                                                                for j in range(i + 1, len(str_list)):
                                                                                                                    for k in range(j + 1, len(str_list)):
                                                                                                                        for l in range(k + 1, len(str_list)):
                                                                                                                            for m in range(l + 1, len(str_list)):
                                                                                                                                ok_list.append(''.join(str_list[i:m + 1]))
    return [list(x) for x in set(ok_list)]