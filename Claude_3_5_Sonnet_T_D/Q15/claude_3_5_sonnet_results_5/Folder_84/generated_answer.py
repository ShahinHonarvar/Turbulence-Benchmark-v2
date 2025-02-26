def sum_odd_ints_inclusive(integer_list):
    start_index = 43
    end_index = 87
    if len(integer_list) <= start_index:
        return 0
    relevant_slice = integer_list[start_index:end_index]
    odd_integers = [num for num in relevant_slice if num % 2 != 0]
    return sum(odd_integers)