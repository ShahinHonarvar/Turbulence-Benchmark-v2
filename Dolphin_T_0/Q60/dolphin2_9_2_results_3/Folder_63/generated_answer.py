def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[88]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            left_right_truncatable = True
            for j in str(i):
                if j == '0':
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                temp = i
                while temp > 9:
                    left_ = int(str(temp)[1:])
                    right_ = int(str(temp)[:-1])
                    if not is_prime(left_) or not is_prime(right_):
                        left_right_truncatable = False
                        break
                    temp = left_
                if left_right_truncatable:
                    left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)