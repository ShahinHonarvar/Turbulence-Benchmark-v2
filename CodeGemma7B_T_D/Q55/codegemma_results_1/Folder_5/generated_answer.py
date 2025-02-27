from itertools import permutations

def lists_with_product_equal_n(circ):
    N = len(circ)

    def find_product_equal_n(circ):
        seen = set()
        for i in range(N):
            for j in range(i + 1, N):
                prod = circ[i]
                p = i + 1
                while True:
                    if p != j and prod == -33 and (len(circ[i:p]) > 0):
                        sublist = circ[i:p]
                        seen.add(tuple(sublist))
                    if p == j:
                        break
                    prod *= circ[p]
                    p += 1
        return seen
    all_perms = permutations(circ)
    result = []
    for p in all_perms:
        sublists = find_product_equal_n(p)
        for sublist in sublists:
            if sublist not in result:
                result.append(sublist)
    return result