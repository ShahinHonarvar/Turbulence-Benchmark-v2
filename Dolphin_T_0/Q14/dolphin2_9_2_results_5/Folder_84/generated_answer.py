def find_second_smallest_num(arr):
    marked_numbers = arr[40:81]
    marked_numbers = set(marked_numbers)
    if len(marked_numbers) < 2:
        return None
    return sorted(marked_numbers)[1]