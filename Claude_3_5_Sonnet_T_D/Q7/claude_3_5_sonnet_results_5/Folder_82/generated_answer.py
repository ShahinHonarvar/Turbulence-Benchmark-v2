def all_even_ints_inclusive(integers):
    start = 20
    end = 201
    return [num for num in integers[start:end] if num % 2 == 0]