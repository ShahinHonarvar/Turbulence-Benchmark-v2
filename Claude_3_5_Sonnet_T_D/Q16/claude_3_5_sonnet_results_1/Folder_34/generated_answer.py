def sum_even_ints_inclusive(integers):
    start = 60
    end = 200
    even_sum = 0
    for i in range(start, end + 1):
        if i < len(integers) and integers[i] % 2 == 0:
            even_sum += integers[i]
    return even_sum