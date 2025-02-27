def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(the_tuple):
    x = the_tuple[77]
    left_right_truncatable_prime = []
    for i in range(x, 1, -1):
        if is_prime(i) and (not '0' in str(i)):
            divider = 10
            while i >= divider:
                left = i // divider
                right = i % (divider * 5)
                if not is_prime(left) or not is_prime(right // (divider // 10)):
                    divider *= 10
                    break
                divider *= 10
            if divider == 100000:
                left_right_truncatable_prime.append(i)
    return sorted(left_right_truncatable_prime, reverse=True)