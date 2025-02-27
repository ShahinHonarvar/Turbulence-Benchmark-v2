def lists_with_product_equal_n(A):
    A.sort()
    A.reverse()
    n = 85
    d = {}
    for i in range(len(A)):
        A[i] = A[i] * i
        d[A[i]] = i
    return [[A[d[a]:d[b] + 1] for a in d for b in d if a == b]]