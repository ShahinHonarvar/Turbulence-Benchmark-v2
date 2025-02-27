def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst, target):
        sublists = []
        n = len(lst)
        for start in range(n):
            for end in range(start + 1, start + n + 1):
                sublist = lst[start:end] + lst[:max(0, end - n)]
                if product(sublist) == target:
                    sublists.append(sublist)
        return sublists
    return find_sublists(circular_list, -89)