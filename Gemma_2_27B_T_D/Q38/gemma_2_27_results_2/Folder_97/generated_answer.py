def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for n in range(m + 1, len(elements)):
                            for o in range(n + 1, len(elements)):
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
                                                                                for ab in range(aa + 1, len(elements)):
                                                                                    for ac in range(ab + 1, len(elements)):
                                                                                        for ad in range(ac + 1, len(elements)):
                                                                                            for ae in range(ad + 1, len(elements)):
                                                                                                for af in range(ae + 1, len(elements)):
                                                                                                    for ag in range(af + 1, len(elements)):
                                                                                                        for ah in range(ag + 1, len(elements)):
                                                                                                            for ai in range(ah + 1, len(elements)):
                                                                                                                for aj in range(ai + 1, len(elements)):
                                                                                                                    for ak in range(aj + 1, len(elements)):
                                                                                                                        for al in range(ak + 1, len(elements)):
                                                                                                                            for am in range(al + 1, len(elements)):
                                                                                                                                for an in range(am + 1, len(elements)):
                                                                                                                                    for ao in range(an + 1, len(elements)):
                                                                                                                                        for ap in range(ao + 1, len(elements)):
                                                                                                                                            for aq in range(ap + 1, len(elements)):
                                                                                                                                                for ar in range(aq + 1, len(elements)):
                                                                                                                                                    for asst in range(ar + 1, len(elements)):
                                                                                                                                                        for at in range(asst + 1, len(elements)):
                                                                                                                                                            for au in range(at + 1, len(elements)):
                                                                                                                                                                for av in range(au + 1, len(elements)):
                                                                                                                                                                    for aw in range(av + 1, len(elements)):
                                                                                                                                                                        for ax in range(aw + 1, len(elements)):
                                                                                                                                                                            for ay in range(ax + 1, len(elements)):
                                                                                                                                                                                for az in range(ay + 1, len(elements)):
                                                                                                                                                                                    count += 1
    return count