def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:16])
    while len(sorted_numbers) < 16:
        next_smallest = min(numbers[len(sorted_numbers) - 16])
        if next_smallest not in sorted_numbers:
            sorted_numbers.append(next_smallest)
    return sorted_numbers[15]