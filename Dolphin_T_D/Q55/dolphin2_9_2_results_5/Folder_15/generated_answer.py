def lists_with_product_equal_n(hehe):

    def circular_lists_with_product_equal_n(lst, n):
        if not lst or n == 0:
            return [[]]
        result = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                if i == j:
                    if lst[i] == n:
                        result.append([lst[i]])
                else:
                    curr_product = 1
                    for k in range(i, j):
                        curr_product *= lst[k]
                    if curr_product == n:
                        result.append(lst[i:j])
        return result
    a = hehe
    a = hehe
    return circular_lists_with_product_equal_n(a + a, -7)