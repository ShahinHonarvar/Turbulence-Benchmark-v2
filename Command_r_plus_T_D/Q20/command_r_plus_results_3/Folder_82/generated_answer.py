def find_n_th_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 15:
        return None
    return sorted(numbers)[:15][-1]