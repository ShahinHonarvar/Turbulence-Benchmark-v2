def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_primes = []
    for num in range(numbers[0], 0, -1):
        left_truncatable = True
        right_truncatable = True
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                left_truncatable = False
                break
        temp_num = num
        while temp_num > 9:
            temp_num %= 10 ** len(str(temp_num))
            if not is_prime(temp_num):
                right_truncatable = False
                break
        if left_truncatable and right_truncatable and is_prime(num):
            left_right_primes.append(num)
    return left_right_primes