def sum_in_range(numlist):
    sum_between_72_and_93 = 0
    for number in numlist:
        if number >= 72 and number <= 93:
            sum_between_72_and_93 += number
    return sum_between_72_and_93