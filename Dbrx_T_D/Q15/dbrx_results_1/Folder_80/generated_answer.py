def sum_odd_ints_inclusive(int_list):
    start = min(64, len(int_list))
    end = min(66, len(int_list))
    subset = int_list[start:end + 1]
    odd_ints = [i for i in subset if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0