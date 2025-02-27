def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d = d + 2
    return d * d > n

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, x + 1):
        left_trimmed = True
        right_trimmed = True
        new_num = num
        while new_num != 0 and new_num != 2 and (new_num != 3) and (new_num != 5) and (new_num != 7):
            new_num = new_num // 10
            if new_num == 0 or not is_prime(new_num):
                left_trimmed = False
        new_num = num
        while new_num != 0 and new_num != 2 and (new_num != 3) and (new_num != 5) and (new_num != 7):
            new_num = new_num % 10
            if new_num == 0 or not is_prime(new_num):
                right_trimmed = False
        if left_trimmed and right_trimmed:
            primes.append(num)
    return sorted(primes, reverse=True)