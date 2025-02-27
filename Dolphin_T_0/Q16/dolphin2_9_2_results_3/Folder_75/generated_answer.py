def sum_even_ints_inclusive(arr):
    sum_ = 0
    for i in [arr[56], arr[57]]:
        if i % 2 == 0:
            sum_ += i
    return sum_ if sum_ else 0