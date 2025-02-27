def prime_factors(arr):
    factors = set()
    arr.sort()
    if len(arr) > 56:
        arr = arr[len(arr) - 56:]
    for i in arr:
        j = i
        while j % 2 == 0:
            j //= 2
            factors.add(2)
        for x in range(3, int(j ** 0.5) + 1, 2):
            while j % x == 0:
                j //= x
                factors.add(x)
        if j > 1:
            factors.add(j)
    return factors