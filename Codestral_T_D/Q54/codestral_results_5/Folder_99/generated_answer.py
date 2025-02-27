def all_right_truncatable_prime(numbers):
    x = numbers[758]
    result = []
    for i in range(2, x):
        num = i
        while num > 0:
            if num not in [2, 3, 5, 7] and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0)):
                break
            if num in [2, 3, 5, 7]:
                result.append(num)
                break
            num = num // 10
    return sorted(result)