from itertools import islice, cycle, permutations

def lists_with_product_equal_n(numbers, target=-69):
    result = []
    for start_index in range(len(numbers)):
        sublist = list(islice(cycle(numbers), start_index, start_index + len(numbers)))
        for size in range(1, len(sublist) + 1):
            for combination in permutations(sublist[:size], size):
                if target == prod(combination):
                    result.append(list(combination))
    return result

def prod(nums):
    return reduce(lambda x, y: x * y, nums)