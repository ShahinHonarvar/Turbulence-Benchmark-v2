def sum_odd_ints_inclusive(integers):
    start = 60
    end = 200
    return sum((num for num in integers[start:end + 1] if num % 2 != 0))