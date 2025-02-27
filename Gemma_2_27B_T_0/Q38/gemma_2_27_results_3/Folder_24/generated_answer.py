def find_subset_of_length_n(elements):
    n = 74
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
                                                                        for aa in range(z + 1, len(elements)):
                                                                            for bb in range(aa + 1, len(elements)):
                                                                                for cc in range(bb + 1, len(elements)):
                                                                                    for dd in range(cc + 1, len(elements)):
                                                                                        for ee in range(dd + 1, len(elements)):
                                                                                            for ff in range(ee + 1, len(elements)):
                                                                                                for gg in range(ff + 1, len(elements)):
                                                                                                    for hh in range(gg + 1, len(elements)):
                                                                                                        for ii in range(hh + 1, len(elements)):
                                                                                                            for jj in range(ii + 1, len(elements)):
                                                                                                                for kk in range(jj + 1, len(elements)):
                                                                                                                    for ll in range(kk + 1, len(elements)):
                                                                                                                        for mm in range(ll + 1, len(elements)):
                                                                                                                            for nn in range(mm + 1, len(elements)):
                                                                                                                                subset = {elements[i], elements[j], elements[k], elements[l], elements[m], elements[o], elements[p], elements[q], elements[r], elements[s], elements[t], elements[u], elements[v], elements[w], elements[x], elements[y], elements[z], elements[aa], elements[bb], elements[cc], elements[dd], elements[ee], elements[ff], elements[gg], elements[hh], elements[ii], elements[jj], elements[kk], elements[ll], elements[mm], elements[nn]}
                                                                                                                                if len(subset) == n:
                                                                                                                                    count += 1
    return count