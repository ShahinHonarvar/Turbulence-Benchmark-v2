def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sublists.append(lst[i:j])
            for j in range(i + 1):
                if i + j + 1 <= n:
                    sublists.append(lst[i:] + lst[:j + 1])
                else:
                    sublists.append(lst[i:] + lst[:j + 1 - n])
        return sublists
    return [sublist for sublist in get_sublists(lst) if product(sublist) == -57]