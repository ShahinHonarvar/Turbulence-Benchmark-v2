def if_perfect_num(lists):
    if lists[99] >= 6 and (lists[99] ** 0.5).is_integer():
        factors = [1]
        for i in range(2, (lists[99] + 1) // 2 + 1):
            if lists[99] % i == 0:
                factors.extend([i, lists[99] // i])
        return sum(factors) - lists[99] == lists[99]
    return False