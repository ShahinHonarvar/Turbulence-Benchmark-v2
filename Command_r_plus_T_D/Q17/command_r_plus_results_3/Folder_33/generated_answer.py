def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-722, -731)
    divisible_by_both = []
    for i in range(281, 695):
        num = numbers_list[i]
        if num % divisor_1 == 0 and num % divisor_2 == 0:
            divisible_by_both.append(num)
    return divisible_by_both