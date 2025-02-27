def sum_odd_ints_inclusive(int_list):
    start, end = (10, 100)
    odd_ints = [i for i in int_list[start:end + 1] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0