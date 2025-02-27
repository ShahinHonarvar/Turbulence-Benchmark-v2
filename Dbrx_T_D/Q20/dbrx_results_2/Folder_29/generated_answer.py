def find_n_th_smallest_num(numbers):
    if len(numbers) < 63:
        return None
    subnumbers = numbers[20:63]
    subnumbers.sort()
    return subnumbers[11]