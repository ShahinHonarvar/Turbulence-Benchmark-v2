def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[:7]:
        if num % 5 == 0 and num % 6 == 0:
            result.append(num)
    return result