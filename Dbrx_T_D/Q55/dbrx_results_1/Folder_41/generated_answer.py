from itertools import islice

def circular_list_permutation(iterable):
    iterators = [iter(iterable)] * len(iterable)
    return zip(*itertools.cycle(iterators))

def lists_with_product_equal_n(numbers, target):
    result = []
    for sublist in circular_list_permutation(numbers):
        for i in range(len(sublist)):
            if reduce(lambda x, y: x * y, sublist[:i + 1]) == target:
                result.append(sublist[:i + 1])
    return result