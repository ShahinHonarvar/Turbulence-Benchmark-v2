from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n):
    result = []
    for i in range(len(numbers)):
        contiguous_product = numbers[i]
        contiguous_numbers = [numbers[i]]
        for j in islice(cycle(range(len(numbers))), i + 1, i + 1 + len(numbers)):
            if contiguous_product * numbers[j] == n and (j not in contiguous_numbers or j == i):
                contiguous_product *= numbers[j]
                contiguous_numbers.append(numbers[j])
                result.append(contiguous_numbers)
                break
            else:
                break
    return result