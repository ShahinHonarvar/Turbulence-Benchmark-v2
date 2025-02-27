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
            for end in range(start + 1, n + 1):
                sublist = lst[start:end]
                if product(sublist) == target:
                    sublists.append(sublist)
                if end > start and end % n == start:
                    break
        return sublists

    def circular_slice(lst, start, end):
        if end <= len(lst):
            return lst[start:end]
        else:
            return lst[start:] + lst[:end % len(lst)]
    n = len(circular_list)
    circular_list += circular_list
    result = find_sublists(circular_list, -83)
    return result