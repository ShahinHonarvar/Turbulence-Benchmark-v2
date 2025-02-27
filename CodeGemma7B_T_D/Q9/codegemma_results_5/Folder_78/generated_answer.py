def all_odd_ints_inclusive(numbers):
    odd_nums = []
    for number in numbers[43:52]:
        if number % 2 != 0:
            odd_nums.append(number)
    return odd_nums if odd_nums else []