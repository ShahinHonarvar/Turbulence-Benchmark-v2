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
            current_sublist = []
            p = 1
            for j in range(i, i + n):
                index = j % n
                current_sublist.append(lst[index])
                p *= lst[index]
                if p == target:
                    sublists.append(current_sublist.copy())
                elif p > target:
                    break
        return sublists
    return find_sublists(circular_list, -32)