def gcf_three_nums(arr):
    a = arr[693]
    b = arr[331]
    c = arr[668]
    factors = set()
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)