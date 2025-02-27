def if_perfect_num(numbers):
    perfect_num = numbers[10]
    perfect_num_divisors = []
    for i in range(1, perfect_num + 1):
        if perfect_num % i == 0:
            perfect_num_divisors.append(i)
    if sum(perfect_num_divisors) == perfect_num:
        return True
    else:
        return False