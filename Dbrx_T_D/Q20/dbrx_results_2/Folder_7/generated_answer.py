def find_n_th_smallest_num(numbers):
    if len(numbers) < 654 or not all((numbers[i] != numbers[i + 1] for i in range(len(numbers) - 1))):
        return None
    sorted_numbers = sorted(numbers[470:655])
    return sorted_numbers[8]