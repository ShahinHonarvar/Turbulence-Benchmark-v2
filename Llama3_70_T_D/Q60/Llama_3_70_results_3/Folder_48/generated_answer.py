def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp_num = str(num)
            left_truncatable = True
            right_truncatable = True
            for _ in range(len(temp_num) - 1):
                if not is_prime(int(temp_num[1:])) or not is_prime(int(temp_num[:-1])):
                    left_truncatable = False
                    right_truncatable = False
                    break
                temp_num = temp_num[1:-1]
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes