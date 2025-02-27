def if_perfect_num(numbers: list) -> bool:
    index = 45
    num = numbers[index]
    sum_divisors = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i == num / i:
                sum_divisors = sum_divisors + i
            else:
                sum_divisors = sum_divisors + i + num / i
            i += 1
    return sum_divisors == num and num != 1