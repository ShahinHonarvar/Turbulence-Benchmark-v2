def composite_nums_between_indices(lst):
    result = set()
    for i in range(len(lst)):
        if i >= 246 and i <= 750:
            num = lst[i]
            if num > 1 and (not num.is_prime()):
                result.add(num)
    return result