def find_n_th_smallest_num(numbers):
    if len(numbers) < 18:
        return None
    else:
        return sorted(numbers[:18])[17]