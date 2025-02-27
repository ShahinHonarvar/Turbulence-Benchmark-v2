def find_subset_of_length_n(s):
    n = 219
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    for m in range(l + 1, len(s)):
                        for o in range(m + 1, len(s)):
                            for p in range(o + 1, len(s)):
                                for q in range(p + 1, len(s)):
                                    for r in range(q + 1, len(s)):
                                        for t in range(r + 1, len(s)):
                                            for u in range(t + 1, len(s)):
                                                for v in range(u + 1, len(s)):
                                                    for w in range(v + 1, len(s)):
                                                        for x in range(w + 1, len(s)):
                                                            for y in range(x + 1, len(s)):
                                                                for z in range(y + 1, len(s)):
                                                                    for aa in range(z + 1, len(s)):
                                                                        for ab in range(aa + 1, len(s)):
                                                                            for ac in range(ab + 1, len(s)):
                                                                                for ad in range(ac + 1, len(s)):
                                                                                    for ae in range(ad + 1, len(s)):
                                                                                        for af in range(ae + 1, len(s)):
                                                                                            for ag in range(af + 1, len(s)):
                                                                                                for ah in range(ag + 1, len(s)):
                                                                                                    for ai in range(ah + 1, len(s)):
                                                                                                        for aj in range(ai + 1, len(s)):
                                                                                                            for ak in range(aj + 1, len(s)):
                                                                                                                for al in range(ak + 1, len(s)):
                                                                                                                    for am in range(al + 1, len(s)):
                                                                                                                        for an in range(am + 1, len(s)):
                                                                                                                            for ao in range(an + 1, len(s)):
                                                                                                                                for ap in range(ao + 1, len(s)):
                                                                                                                                    for aq in range(ap + 1, len(s)):
                                                                                                                                        for ar in range(aq + 1, len(s)):
                                                                                                                                            for as_ in range(ar + 1, len(s)):
                                                                                                                                                for at in range(as_ + 1, len(s)):
                                                                                                                                                    for au in range(at + 1, len(s)):
                                                                                                                                                        for av in range(au + 1, len(s)):
                                                                                                                                                            for aw in range(av + 1, len(s)):
                                                                                                                                                                for ax in range(aw + 1, len(s)):
                                                                                                                                                                    for ay in range(ax + 1, len(s)):
                                                                                                                                                                        for az in range(ay + 1, len(s)):
                                                                                                                                                                            subset = {s[i], s[j], s[k], s[l], s[m], s[o], s[p], s[q], s[r], s[t], s[u], s[v], s[w], s[x], s[y], s[z], s[aa], s[ab], s[ac], s[ad], s[ae], s[af], s[ag], s[ah], s[ai], s[aj], s[ak], s[al], s[am], s[an], s[ao], s[ap], s[aq], s[ar], s[as_], s[at], s[au], s[av], s[aw], s[ax], s[ay], s[az]}
                                                                                                                                                                            if len(subset) == n:
                                                                                                                                                                                count += 1
    return count