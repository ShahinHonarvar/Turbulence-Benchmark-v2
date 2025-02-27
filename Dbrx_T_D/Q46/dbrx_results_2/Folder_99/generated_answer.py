def gcf_three_nums(numbers):
    if len(numbers) < 3:
        return 'The list should contain at least three elements.'
    index_numbers = [numbers[912], numbers[170], numbers[500]]
    index_numbers = [i for i in index_numbers if i > 0]

    def compute_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    gcf = compute_gcf(compute_gcf(index_numbers[0], index_numbers[1]), index_numbers[2])
    return gcf