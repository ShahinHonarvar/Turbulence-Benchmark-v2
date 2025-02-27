def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        num_slice = numbers[:5]
        return sorted(num_slice)[-2] if len(set(num_slice)) > 1 else None