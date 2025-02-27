def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            trunc_left_right = num_str[i:len(num_str) - i]
            if len(trunc_left_right) < 2 and trunc_left_right != '2' and (trunc_left_right != '3') and (trunc_left_right != '5') and (trunc_left_right != '7'):
                is_truncatable = False
                break
            if not is_prime(int(trunc_left_right)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes