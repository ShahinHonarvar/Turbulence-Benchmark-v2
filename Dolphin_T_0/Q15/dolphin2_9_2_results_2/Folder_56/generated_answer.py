def sum_odd_ints_inclusive(arr):
    to_sum = [i for i in arr if i % 2 != 0][0:1]
    return sum(to_sum) if to_sum else 0