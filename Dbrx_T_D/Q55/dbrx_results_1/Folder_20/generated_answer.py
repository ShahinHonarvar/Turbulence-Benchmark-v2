from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def circular_list_slice(circular_list, start, end):
        return [x for i, x in islice(enumerate(circular_list), start, end)]

    def sublists_with_product_equal_n(numbers, target):
        result = []
        product = 1
        i = 0
        for j in range(len(numbers)):
            product *= numbers[j]
            while product > target and i <= j:
                product //= numbers[i]
                i += 1
            if product == target:
                result.append(circular_list_slice(numbers, i, j + 1))
        return result
    return sublists_with_product_equal_n(cycle(numbers), -69)