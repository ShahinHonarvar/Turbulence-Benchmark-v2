def sum_even_ints_inclusive(arr):
    count = 0
    sum = 0
    for i in range(31, 73):
        if i != len(arr) and arr[i] % 2 == 0:
            count += 1
            sum += int(arr[i])
    if count == 0:
        return 0
    else:
        return sum