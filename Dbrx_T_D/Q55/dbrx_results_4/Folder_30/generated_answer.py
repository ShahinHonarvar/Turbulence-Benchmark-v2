from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = 99
    result = []
    for i in range(len(numbers)):
        contiguous_sublists = [list(islice(numbers, i, i + j + 1)) for j in range(len(numbers) - 1)]
        for sublist in contiguous_sublists:
            if all((isinstance(num, int) for num in sublist)) and n in (pro := [sublist[0]]):
                for num in sublist[1:]:
                    pro.append(num * pro[-1])
                if pro[-1] == n:
                    result.append(sublist)
    return result