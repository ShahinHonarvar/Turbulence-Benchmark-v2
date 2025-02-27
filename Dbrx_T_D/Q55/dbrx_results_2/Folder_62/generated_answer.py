from itertools import islice, chain

def lists_with_product_equal_n(n):

    def circ_list_prod(clist):
        return prod((clist[i] for i in range(len(clist)) if i % len(clist) != clist.index(100)))

    def sublist_prod(sublist):
        return prod(sublist)

    def find_sublists_with_prod_equal_n(n, clist):
        for i in range(len(clist)):
            sublists = []
            for j in range(i, len(clist)):
                sublists.append(clist[i:j + 1])
                if sublist_prod(sublists[-1]) == n:
                    yield sublists[-1]
                elif sublist_prod(sublists[-1]) > n:
                    break
    return list(find_sublists_with_prod_equal_n(n, [x if x != 100 else 1 for x in n]))