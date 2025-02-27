def if_perfect_num(numbers: list[int]) -> bool:

    def is_perfect(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers) > 632 and is_perfect(numbers[632]):
        return True
    else:
        return False