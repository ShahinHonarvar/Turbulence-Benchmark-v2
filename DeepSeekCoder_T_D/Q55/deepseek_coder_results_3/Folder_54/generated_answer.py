def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        n = len(lst)
        result = []
        for start in range(n):
            for end in range(start + 1, n + 1):
                sub = lst[start:end]
                if product(sub) == -17:
                    result.append(sub)
        return result
    n = len(circular_list)
    circular_list += circular_list
    all_sublists = find_sublists(circular_list)
    unique_sublists = []
    seen = set()
    for sublist in all_sublists:
        if tuple(sublist) not in seen:
            unique_sublists.append(sublist)
            seen.add(tuple(sublist))
    return unique_sublists