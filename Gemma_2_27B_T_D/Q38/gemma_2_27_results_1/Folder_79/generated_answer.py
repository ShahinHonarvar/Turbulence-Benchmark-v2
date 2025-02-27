def find_subset_of_length_n(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                for l in range(k + 1, len(data)):
                    for m in range(l + 1, len(data)):
                        for n in range(m + 1, len(data)):
                            for o in range(n + 1, len(data)):
                                for p in range(o + 1, len(data)):
                                    for q in range(p + 1, len(data)):
                                        for r in range(q + 1, len(data)):
                                            for s in range(r + 1, len(data)):
                                                for t in range(s + 1, len(data)):
                                                    for u in range(t + 1, len(data)):
                                                        for v in range(u + 1, len(data)):
                                                            for w in range(v + 1, len(data)):
                                                                for x in range(w + 1, len(data)):
                                                                    for y in range(x + 1, len(data)):
                                                                        for z in range(y + 1, len(data)):
                                                                            for aa in range(z + 1, len(data)):
                                                                                for ab in range(aa + 1, len(data)):
                                                                                    for ac in range(ab + 1, len(data)):
                                                                                        for ad in range(ac + 1, len(data)):
                                                                                            for ae in range(ad + 1, len(data)):
                                                                                                for af in range(ae + 1, len(data)):
                                                                                                    for ag in range(af + 1, len(data)):
                                                                                                        for ah in range(ag + 1, len(data)):
                                                                                                            for ai in range(ah + 1, len(data)):
                                                                                                                for aj in range(ai + 1, len(data)):
                                                                                                                    for ak in range(aj + 1, len(data)):
                                                                                                                        for al in range(ak + 1, len(data)):
                                                                                                                            for am in range(al + 1, len(data)):
                                                                                                                                for an in range(am + 1, len(data)):
                                                                                                                                    for ao in range(an + 1, len(data)):
                                                                                                                                        for ap in range(ao + 1, len(data)):
                                                                                                                                            for aq in range(ap + 1, len(data)):
                                                                                                                                                for ar in range(aq + 1, len(data)):
                                                                                                                                                    for as_ in range(ar + 1, len(data)):
                                                                                                                                                        for at in range(as_ + 1, len(data)):
                                                                                                                                                            for au in range(at + 1, len(data)):
                                                                                                                                                                for av in range(au + 1, len(data)):
                                                                                                                                                                    for aw in range(av + 1, len(data)):
                                                                                                                                                                        for ax in range(aw + 1, len(data)):
                                                                                                                                                                            count += 1
    return count