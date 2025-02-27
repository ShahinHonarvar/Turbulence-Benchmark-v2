def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(inputs):
    results = []
    x = inputs[22]
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                if not is_prime(j):
                    break
                j = j // 10
                if j > 0:
                    results.append(i)
                    break
    return sorted(results, reverse=True)