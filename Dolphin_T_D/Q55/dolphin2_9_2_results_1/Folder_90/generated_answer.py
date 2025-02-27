import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    extend_lst = lst + lst[:-1]
    sublist_with_product_n = []
    for length in range(1, n + 1):
        for i in range(n):
            for join_cycle in itertools.product(lst, repeat=length - 1):
                sublist = [extend_lst[i]] + list(join_cycle)
                if sublist[-1] == extend_lst[i + length - 1]:
                    if sublist_with_product_n and sublist_with_product_n[-1] == sublist:
                        break
                    product = 1
                    for j in sublist:
                        product *= j
                    if product == -690:
                        sublist_with_product_n.append(sublist)
    return sublist_with_product_n