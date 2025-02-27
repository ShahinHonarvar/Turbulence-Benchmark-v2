def palindrome_of_length_n(x):
    set1 = set()
    for i in range(len(x) - 41):
        for j in range(i + 12, len(x) - 30):
            for k in range(j + 8, len(x) - 22):
                for l in range(k + 6, len(x) - 16):
                    for m in range(l + 4, len(x) - 12):
                        for n in range(m + 2, len(x) - 10):
                            for o in range(n + 2, len(x) - 8):
                                for p in range(o + 2, len(x) - 6):
                                    for q in range(p + 2, len(x) - 4):
                                        for r in range(q + 2, len(x) - 2):
                                            for s in range(r + 2, len(x) - 2):
                                                if x[i:j + 3] == x[j:k + 7][::-1] == x[k:l + 5][::-1] == x[l:m + 3][::-1] == x[m:n + 1][::-1] == x[n:o + 1][::-1] == x[o:p + 1][::-1] == x[p:q + 1][::-1] == x[q:r + 1][::-1] == x[r:s + 1][::-1] == x[s:j + 3][::-1] and x[j:k + 7].isalnum() and x[k:l + 5].isalnum() and x[l:m + 3].isalnum() and x[m:n + 1].isalnum() and x[n:o + 1].isalnum() and x[o:p + 1].isalnum() and x[p:q + 1].isalnum() and x[q:r + 1].isalnum() and x[r:s + 1].isalnum() and x[s:j + 3].isalnum():
                                                    set1.add(x[i:j + 3])
    return set1