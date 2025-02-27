def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 36):
        for j in range(i + 1, len(str) - 35):
            for k in range(j + 1, len(str) - 34):
                for l in range(k + 1, len(str) - 33):
                    for m in range(l + 1, len(str) - 32):
                        for n in range(m + 1, len(str) - 31):
                            for o in range(n + 1, len(str) - 30):
                                for p in range(o + 1, len(str) - 29):
                                    for q in range(p + 1, len(str) - 28):
                                        for r in range(q + 1, len(str) - 27):
                                            for s in range(r + 1, len(str) - 26):
                                                for t in range(s + 1, len(str) - 25):
                                                    for u in range(t + 1, len(str) - 24):
                                                        for v in range(u + 1, len(str) - 23):
                                                            for w in range(v + 1, len(str) - 22):
                                                                for x in range(w + 1, len(str) - 21):
                                                                    for y in range(x + 1, len(str) - 20):
                                                                        for z in range(y + 1, len(str) - 19):
                                                                            for aa in range(z + 1, len(str) - 18):
                                                                                for bb in range(aa + 1, len(str) - 17):
                                                                                    for cc in range(bb + 1, len(str) - 16):
                                                                                        for dd in range(cc + 1, len(str) - 15):
                                                                                            for ee in range(dd + 1, len(str) - 14):
                                                                                                for ff in range(ee + 1, len(str) - 13):
                                                                                                    for gg in range(ff + 1, len(str) - 12):
                                                                                                        for hh in range(gg + 1, len(str) - 11):
                                                                                                            for ii in range(hh + 1, len(str) - 10):
                                                                                                                for jj in range(ii + 1, len(str) - 9):
                                                                                                                    for kk in range(jj + 1, len(str) - 8):
                                                                                                                        for ll in range(kk + 1, len(str) - 7):
                                                                                                                            for mm in range(ll + 1, len(str) - 6):
                                                                                                                                for nn in range(mm + 1, len(str) - 5):
                                                                                                                                    for oo in range(nn + 1, len(str) - 4):
                                                                                                                                        for pp in range(oo + 1, len(str) - 3):
                                                                                                                                            for qq in range(pp + 1, len(str) - 2):
                                                                                                                                                for rr in range(qq + 1, len(str) - 1):
                                                                                                                                                    for ss in range(rr + 1, len(str)):
                                                                                                                                                        if len(set(str[i:ss + 1])) == 37:
                                                                                                                                                            result.add(str[i:ss + 1])
    return list(result)