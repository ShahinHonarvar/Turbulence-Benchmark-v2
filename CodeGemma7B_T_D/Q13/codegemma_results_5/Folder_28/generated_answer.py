def find_second_largest_num(arr):
    if len(arr) <= 63 or not all((isinstance(num, int) for num in arr)):
        raise ValueError('Invalid input. The list should have at least 64 elements containing only integers.')
    sorted_arr = sorted(arr[62:64], reverse=True)
    return sorted_arr[1] if len(sorted_arr) > 1 else 'None'