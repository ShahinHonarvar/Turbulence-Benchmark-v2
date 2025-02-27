def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = set()
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        temp = str_num
        while len(temp) > 1:
            temp = temp[1:-1]
            if not is_prime(int(temp)):
                break
        else:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)