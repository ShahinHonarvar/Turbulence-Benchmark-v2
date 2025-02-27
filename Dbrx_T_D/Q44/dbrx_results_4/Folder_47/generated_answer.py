from math import sqrt

def composite_nums_between_indices(n: list) -> set:
    if len(n) < 89:
        return set()
    composite_numbers = set()
    for num in n[75:89]:
        if num > 1:
            is_composite = False
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(num)
    return composite_numbers