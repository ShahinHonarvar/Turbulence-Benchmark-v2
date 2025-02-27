def all_neg_ints_inclusive(numbers):
    neg_ints = []
    for num in numbers[22:51]:
        if num <= 0:
            neg_ints.append(num)
    return neg_ints