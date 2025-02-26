def sum_odd_ints_inclusive(integers):
    end = min(len(integers), 98)
    return sum((num for num in integers[59:end] if num % 2 != 0))