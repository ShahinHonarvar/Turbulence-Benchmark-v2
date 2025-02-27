def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst, target):
        sublists = []
        n = len(lst)
        for i in range(n):
            current_product = 1
            for j in range(i, i + n):
                current_product *= lst[j % n]
                if current_product == target:
                    sublists.append(lst[i:j + 1] if j < n else lst[i:] + lst[:j + 1 - n])
        return sublists
    return find_sublists(circular_list, -83)