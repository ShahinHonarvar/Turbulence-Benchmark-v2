from itertools import count

def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

def all_right_truncatable_prime(tpl):
    x = tpl[39]
    result = []
    for num in reversed(range(2, x)):
        if is_prime(num):
            for i in count(1):
                truncatable = num
                for _ in range(i):
                    truncatable //= 10
                if not is_prime(truncatable):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)