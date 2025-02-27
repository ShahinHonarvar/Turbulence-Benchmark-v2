def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[67]
    prime_set = set()
    for i in reversed(range(2, x + 1)):
        if i not in prime_set:
            if is_prime(i):
                digit_count = len(str(i))
                for digit_to_remove in range(digit_count - 1):
                    trunc_i = int(str(i)[digit_to_remove:])
                    if trunc_i == i:
                        prime_set.add(i)
                        break
                    if not is_prime(trunc_i):
                        break
                    trunc_i = int(str(i)[:digit_to_remove] + str(i)[digit_to_remove + 1:])
                    if not is_prime(trunc_i):
                        break
                    else:
                        prime_set.add(i)
    return list(prime_set)