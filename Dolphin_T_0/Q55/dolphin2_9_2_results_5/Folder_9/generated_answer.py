def lists_with_product_equal_n(n, lst):

    def find_sublists(idx, product, sublist, n, visited):
        if product == n and idx not in visited:
            res.append(list(sublist))
            visited.add(idx)
        elif product != 1 and -n <= product <= n and (idx < len(lst)):
            for i in range(idx + 1, len(lst) + 1):
                if i == len(lst):
                    find_sublists(0, product // lst[idx], sublist, n, visited)
                else:
                    find_sublists(i, product * lst[idx], sublist + [lst[idx]], n, visited)
                if i < len(lst):
                    sublist.pop()
    res = []
    visited = set()
    if lst:
        find_sublists(0, 1, [], n, visited)
    return res