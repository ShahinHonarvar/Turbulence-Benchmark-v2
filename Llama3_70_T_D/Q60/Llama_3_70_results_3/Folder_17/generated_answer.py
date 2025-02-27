def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = set()
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = str(num)
            is_truncatable = True
            while len(temp) > 1:
                temp = temp[1:-1]
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)