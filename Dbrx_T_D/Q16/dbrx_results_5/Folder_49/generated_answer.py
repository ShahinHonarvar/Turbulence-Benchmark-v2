def sum_even_ints_inclusive(int_list):
    start_index = 8
    end_index = 80
    if len(int_list) <= end_index:
        return 'Input list is not long enough'
    else:
        even_ints = [i for i in int_list[start_index:end_index + 1] if i % 2 == 0]
        if even_ints:
            return sum(even_ints)
        else:
            return 0