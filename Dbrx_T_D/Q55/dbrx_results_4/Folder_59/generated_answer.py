from itertools import islice

def circular_list(iterable):
    l = list(iterable)
    return l + [l[0]] if l else []

def lists_with_product_equal_n(n):

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)

    def sublists_with_product(lst, target):
        if not lst:
            return []
        elif product(lst) == target:
            return [tuple(lst)]
        elif product(lst) < target or not all((x > target for x in lst)):
            return [(head,) + tail for head in lst[:1] for tail in sublists_with_product(lst[1:], target)]
        else:
            return []

    def circular_sublists_with_product(lst, target):
        return [lst[i:] + lst[:i] for i in range(len(lst)) if product(lst[i:]) == target]

    def all_sublists_with_product(lst, target):
        return [sublist for sublist in sublists_with_product(lst, target) + circular_sublists_with_product(lst, target) if any((x != 0 for x in sublist)) if not any((all((x < 0 for x in xlist)) for xlist in sublists_with_product(sublist, -target) + circular_sublists_with_product(sublist, -target)))]

    def all_lists_with_product(lst, target):
        return [sublst for sublst in all_sublists_with_product(lst, target) + all_sublists_with_product(lst, -target) if product(sublst) == target]
    return all_lists_with_product(circular_list(n), -3)