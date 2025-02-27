import itertools

def get_next_index(a, i):
    return i + 1 % len(a)

def sublist_product(a):
    product = 1
    for i in a:
        product *= i
    return product

def all_sublists(a):
    sublists = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sublists.append(a[i:j])
    return sublists

def lists_with_product_equal_n(x, a):
    a = list(itertools.islice(all_sublists(a), 1, len(a) + 1))
    sublists = [i for i in a if sublist_product(i) == x]
    return sublists