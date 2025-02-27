def all_right_truncatable_prime(t):
    x = t[57]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            flag = True
            for digit in str(num)[::-1][1:]:
                if not is_prime(int(str(num)[::-1][:digit])):
                    flag = False
                    break
            if flag:
                right_truncutable_primes.append(num)
    return sorted(right_truncutable_primes, reverse=True)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True