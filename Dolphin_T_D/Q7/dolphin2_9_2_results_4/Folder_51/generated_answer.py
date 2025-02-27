def all_even_ints_inclusive(arr):
    even_numbers = []
    for i in range(1, 9):
        if arr[i] % 2 == 0:
            even_numbers.append(arr[i])
    return even_numbers