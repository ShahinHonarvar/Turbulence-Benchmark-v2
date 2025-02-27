def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    trunc_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and (not '0' in str(num)):
            trunc_num = num
            while trunc_num > 0 and len(str(trunc_num)) > 1:
                trunc_num = int(str(trunc_num)[1:-1])
                if not is_prime(trunc_num):
                    break
            if trunc_num > 0 and (len(str(trunc_num)) == 1 or is_prime(trunc_num)):
                trunc_primes.append(num)
    return sorted(list(set(trunc_primes)), reverse=True)