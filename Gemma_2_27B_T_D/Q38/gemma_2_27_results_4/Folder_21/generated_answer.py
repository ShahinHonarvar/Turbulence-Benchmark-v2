def find_subset_of_length_n(elements):
    n = 722
    subsets = 0
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
                                                                        if i != j and i != k and (i != l) and (i != m) and (i != o) and (i != p) and (i != q) and (i != r) and (i != s) and (i != t) and (i != u) and (i != v) and (i != w) and (i != x) and (i != y) and (i != z) and (j != k) and (j != l) and (j != m) and (j != o) and (j != p) and (j != q) and (j != r) and (j != s) and (j != t) and (j != u) and (j != v) and (j != w) and (j != x) and (j != y) and (j != z) and (k != l) and (k != m) and (k != o) and (k != p) and (k != q) and (k != r) and (k != s) and (k != t) and (k != u) and (k != v) and (k != w) and (k != x) and (k != y) and (k != z) and (l != m) and (l != o) and (l != p) and (l != q) and (l != r) and (l != s) and (l != t) and (l != u) and (l != v) and (l != w) and (l != x) and (l != y) and (l != z) and (m != o) and (m != p) and (m != q) and (m != r) and (m != s) and (m != t) and (m != u) and (m != v) and (m != w) and (m != x) and (m != y) and (m != z) and (o != p) and (o != q) and (o != r) and (o != s) and (o != t) and (o != u) and (o != v) and (o != w) and (o != x) and (o != y) and (o != z) and (p != q) and (p != r) and (p != s) and (p != t) and (p != u) and (p != v) and (p != w) and (p != x) and (p != y) and (p != z) and (q != r) and (q != s) and (q != t) and (q != u) and (q != v) and (q != w) and (q != x) and (q != y) and (q != z) and (r != s) and (r != t) and (r != u) and (r != v) and (r != w) and (r != x) and (r != y) and (r != z) and (s != t) and (s != u) and (s != v) and (s != w) and (s != x) and (s != y) and (s != z) and (t != u) and (t != v) and (t != w) and (t != x) and (t != y) and (t != z) and (u != v) and (u != w) and (u != x) and (u != y) and (u != z) and (v != w) and (v != x) and (v != y) and (v != z) and (w != x) and (w != y) and (w != z) and (x != y) and (x != z) and (y != z):
                                                                            subsets += 1
    return subsets