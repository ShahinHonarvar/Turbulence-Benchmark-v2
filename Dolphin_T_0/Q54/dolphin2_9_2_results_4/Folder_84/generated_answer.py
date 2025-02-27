def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[630]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = num
            while truncated_num >= 10:
                truncated_num = truncated_num // 10
                if not is_prime(truncated_num):
                    break
                else:
                    right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)