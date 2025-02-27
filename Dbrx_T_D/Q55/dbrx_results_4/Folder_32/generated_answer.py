from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=76):

    def product_business(sublist):
        return list(islice(accumulate(product(sublist), lambda x, y: x * y % n, initial=1), len(sublist)))
    return [sublist for i in range(len(lst)) for sublist in itertools.combinations(lst, i) if product_business(sublist)[0] == 1 and product_business(sublist)[-1] == 1]