def all_left_truncatable_prime(numbers):
    for num in numbers:
        if num % 2 == 0 or num % 3 == 0:
            continue
        if '0' in str(num):
            continue
        temp = num // 10
        is_prime = True
        while temp > 1:
            if temp % 2 == 0 or temp % 3 == 0:
                is_prime = False
                break
            temp //= 10
        if is_prime:
            yield num