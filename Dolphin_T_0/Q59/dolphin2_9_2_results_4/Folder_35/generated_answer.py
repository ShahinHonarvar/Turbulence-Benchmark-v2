def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    result = []
    for i in range(2, x):
        if is_prime(i):
            k = i
            while k != 0:
                if not is_prime(k):
                    break
                k //= 10
                if k != 0 and k in result:
                    break
            else:
                result.append(i)
    return sorted(result)