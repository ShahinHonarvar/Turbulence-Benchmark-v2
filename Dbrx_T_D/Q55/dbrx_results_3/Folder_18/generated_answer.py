from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=36):
    result = []
    for i in range(len(numbers)):
        window = numbers[i:i + len(numbers)]
        for j in range(1, len(window) + 1):
            sub_list = list(islice(cycle(window), j))
            if len(sub_list) == 1:
                if sub_list[0] == n:
                    result.append(sub_list)
            elif sub_list[0] * sub_list[-1] == n:
                result.append(sub_list)
    return result