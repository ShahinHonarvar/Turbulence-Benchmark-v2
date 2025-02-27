def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        n = len(lst)
        result = []
        for i in range(n):
            for j in range(i + 1, n + i + 1):
                sub = lst[i:j] if j <= n else lst[i:] + lst[:j - n]
                if product(sub) == 10:
                    result.append(sub)
        return result
    return find_sublists(circular_list)