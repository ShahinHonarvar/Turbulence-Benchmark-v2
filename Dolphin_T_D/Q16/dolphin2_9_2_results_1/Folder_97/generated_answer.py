def sum_even_ints_inclusive(ints):
    sum = 0
    for num in ints[40:81]:
        if num % 2 == 0:
            sum += num
    return sum if sum != 0 else 0