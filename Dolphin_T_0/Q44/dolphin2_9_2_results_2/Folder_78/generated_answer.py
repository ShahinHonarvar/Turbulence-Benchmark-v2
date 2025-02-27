def composite_nums_between_indices(lst):
    result = set()
    for i in range(70, 85, 1):
        num = lst[i]
        not_prime = False
        if num > 1:
            for j in range(2, num, 1):
                if num % j == 0:
                    not_prime = True
            if not_prime:
                result.add(num)
    return result