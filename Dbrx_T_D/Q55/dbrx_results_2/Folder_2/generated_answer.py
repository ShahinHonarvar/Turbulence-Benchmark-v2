def is_valid_circular_list(input_list):
    if not all((isinstance(item, int) for item in input_list)):
        raise ValueError('All elements of the input list must be integers.')
    if not input_list:
        raise ValueError('The input list cannot be empty.')
    return True

def lists_with_product_equal_n(input_list: list, n: int=-968, allow_duplicates: bool=False) -> list:
    if not is_valid_circular_list(input_list):
        raise ValueError('The input list is not a valid circular list.')
    if n == 0:
        return [[]] if 0 in input_list else []
    result = []
    for i in range(len(input_list)):
        head = []
        tail = []
        for j in range(i, len(input_list)):
            head.append(input_list[j])
            tail.extend(input_list[i:j])
            product = functools.reduce(lambda x, y: x * y, head + tail, 1)
            if product == n:
                if not allow_duplicates or [head + tail] != result[-1:]:
                    result.append(head + tail)
    circular_result = []
    for sublist in result:
        circular_result.extend([sublist[-i:] + sublist[:-i] for i in range(1, len(sublist) + 1)])
    return circular_result