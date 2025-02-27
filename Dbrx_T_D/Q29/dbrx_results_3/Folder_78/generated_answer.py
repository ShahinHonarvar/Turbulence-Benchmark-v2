def gcf_two_nums(numbers):
    first_num = numbers[13]
    second_num = numbers[54]
    for i in range(min(first_num, second_num), 0, -1):
        if first_num % i == 0 and second_num % i == 0:
            return i