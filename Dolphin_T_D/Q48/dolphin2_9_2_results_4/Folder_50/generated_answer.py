def return_binary_or_hexa(arr):
    a = arr[13]
    b = arr[76]
    integers = set(range(a + 1, b))
    tuple_integers = set(arr[13:77])
    missing_integers = integers - tuple_integers
    sum_integers = sum(missing_integers)
    if sum_integers % 2 == 1:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:].upper()