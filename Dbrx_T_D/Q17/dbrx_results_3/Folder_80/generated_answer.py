def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(max(14, numbers[13] // 71 * 71 - 1), min(len(numbers) - 1, numbers[93] // 81 * 81 + 1)):
        if numbers[i] % 71 == 0 and numbers[i] % 81 == 0:
            result.append(numbers[i])
    return result