def all_left_truncatable_prime(numbers):
    x = numbers[84]
    result = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            left_truncatable = [num]
            while num != 0:
                num = int(str(num)[1:])
                if num and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                    left_truncatable.append(num)
            if num in left_truncatable:
                result.append(num)
    return sorted(result)