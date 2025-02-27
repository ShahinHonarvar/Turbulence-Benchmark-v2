def find_subset_of_length_n(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    for m in range(l + 1, len(s)):
                        for n in range(m + 1, len(s)):
                            for o in range(n + 1, len(s)):
                                for p in range(o + 1, len(s)):
                                    for q in range(p + 1, len(s)):
                                        for r in range(q + 1, len(s)):
                                            count += 1
    return count