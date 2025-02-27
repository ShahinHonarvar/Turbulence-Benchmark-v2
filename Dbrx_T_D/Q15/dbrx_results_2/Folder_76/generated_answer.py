def sum_odd_ints_inclusive(integer_list):
    start, end = (686, 987)
    odd_ints = [i for i in integer_list[start:end + 1] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0