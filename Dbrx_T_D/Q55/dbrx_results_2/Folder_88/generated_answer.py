from itertools import islice, cycle

def lists_with_product_equal_n(nums):

    def match_sub(num):
        acc, sub = (1, [])
        for n in nums:
            while num % n != 0 and acc > 1:
                acc //= sub.pop()
            sub.append(n)
            acc *= n
            if acc == -56:
                yield sub
    for sub in (match_sub(n) for n in range(1, 8)):
        yield from sub

def circular_list_sublists(nums):
    return [list(islice(cycle(nums), i, i)) for i in range(1, len(nums))]

def filter_matchings(sublists, matchings):
    result = set()
    for matching in matchings:
        for sub in sublists:
            if set(sub) == set(matching):
                result.add(tuple(sub))
    return list(result)

def lists_with_product_equal_n_circular(nums):
    sublists = circular_list_sublists(nums)
    matchings = lists_with_product_equal_n(sublists)
    return filter_matchings(sublists, matchings)