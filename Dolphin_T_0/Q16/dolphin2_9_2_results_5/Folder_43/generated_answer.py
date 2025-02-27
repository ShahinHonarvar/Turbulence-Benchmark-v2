def sum_even_ints_inclusive(arr):
    sum = 0
    for num in arr[68:87]:
        if num % 2 == 0:
            sum += num
    return sum