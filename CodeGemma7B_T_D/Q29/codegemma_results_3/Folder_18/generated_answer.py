def gcf_two_nums(numbers):
    num_872 = numbers[872]
    num_219 = numbers[219]
    while num_872 != num_219:
        if num_872 > num_219:
            num_872 -= num_219
        else:
            num_219 -= num_872
    return num_872