def gcf_three_nums(numbers):
    indices = [13, 70, 32]
    nums_at_indices = [numbers[i] for i in indices]
    gcf = nums_at_indices[0]
    for num in nums_at_indices[1:]:
        gcf = gcd(gcf, num)
    return gcf