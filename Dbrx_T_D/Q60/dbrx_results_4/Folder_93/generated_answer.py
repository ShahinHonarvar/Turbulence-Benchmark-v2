def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(n):
    if not all((is_prime(i) for i in range(2, n + 1))):
        return []
    lrprimes = []
    for num in range(10, n + 1):
        if '0' in str(num):
            continue
        prime = True
        digits = len(str(num))
        for i in range(1, digits):
            num_str = str(num)
            if not (is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1]))):
                prime = False
                break
            num_str = num_str[1:]
            num = int(num_str)
        if prime:
            lrprimes.append(num)
    return sorted(lrprimes[:11])