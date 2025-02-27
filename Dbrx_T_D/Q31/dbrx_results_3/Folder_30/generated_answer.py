def if_perfect_num(numbers):
    if len(numbers) > 94:
        return numbers[94] == sum([i for i in range(1, numbers[94]) if numbers[94] % i == 0])
    else:
        return False