def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    result = []
    queue = [str(p) for p in range(1, 10) if is_prime(p)]
    while queue:
        num = queue.pop(0)
        if int(num) < x:
            if is_prime(int(num)):
                result.append(int(num))
                for i in range(1, 10):
                    if '0' not in num:
                        new_num = str(i) + num
                        if is_prime(int(new_num)):
                            queue.append(new_num)
    return result

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    return sorted(left_truncatable_primes(x))