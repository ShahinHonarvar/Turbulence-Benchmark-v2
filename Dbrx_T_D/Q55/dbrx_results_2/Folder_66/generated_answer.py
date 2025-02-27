from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n=78):

    def sublists_with_product_equal_n(sublist, n):
        if not sublist:
            return [[]] if n == 1 else []
        else:
            head = sublist[0]
            tail = sublist[1:]
            return sublists_with_product_equal_n(tail, n) + sublists_with_product_equal_n(tail, n // head) + [[head] + sl for sl in sublists_with_product_equal_n(tail, n // head) if n % head == 0]
    circular_list_size = len(circular_list)
    if circular_list_size == 0:
        return []
    elif circular_list_size == 1:
        return [circular_list] if circular_list[0] == n else []
    sublists = sublists_with_product_equal_n(circular_list, n)
    circular_sublists = [[circular_list[i % circular_list_size] for i in range(j, j + len(sublist))] for j, sublist in enumerate(sublists)]
    return circular_sublists