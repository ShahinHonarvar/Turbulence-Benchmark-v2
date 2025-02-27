def sum_of_divisors_in_range(num: int) -> int:
    result = 0
    for i in range(469, 683):
        if num % i == 0:
            result += i
    return result