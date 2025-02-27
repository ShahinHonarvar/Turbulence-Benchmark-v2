def sum_odd_ints_inclusive(input_list):
    start, end = (17, 78)
    odd_ints = [i for i in input_list[start:end + 1] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0