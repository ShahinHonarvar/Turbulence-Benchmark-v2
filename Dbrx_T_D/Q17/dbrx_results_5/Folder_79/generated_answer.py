def all_ints_div_by_both_two_nums(numbers):
    start = 8
    end = 9
    div_by_both = []
    for i in range(start, end + 1):
        if i < 0 or i >= len(numbers):
            continue
        num = numbers[i]
        if num % -3 == 0 and num % 6 == 0:
            div_by_both.append(num)
    return div_by_both