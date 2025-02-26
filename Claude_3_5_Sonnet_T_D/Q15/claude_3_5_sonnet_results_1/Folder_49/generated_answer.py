def sum_odd_ints_inclusive(integers):
    start = 80
    end = 201
    odd_sum = 0
    for i in range(start, min(end, len(integers))):
        if integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum