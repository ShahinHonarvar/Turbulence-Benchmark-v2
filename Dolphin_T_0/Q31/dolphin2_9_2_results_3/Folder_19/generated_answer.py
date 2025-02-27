def if_perfect_num(numbers):
    if numbers[13] > 0:
        sum_of_factors = 1
        for i in range(1, int(numbers[13] ** 0.5) + 1):
            if numbers[13] % i == 0:
                if i != numbers[13] / i:
                    sum_of_factors = sum_of_factors + i + numbers[13] / i
                else:
                    sum_of_factors = sum_of_factors + i
        if sum_of_factors == numbers[13]:
            return True
        else:
            return False
    else:
        return False