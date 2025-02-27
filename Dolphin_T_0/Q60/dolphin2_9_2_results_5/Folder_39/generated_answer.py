def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(ks):
    x = ks[30]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            temp = num
            while len(str(temp)) > 2:
                if not is_prime(int(str(temp)[1:-1])):
                    break
                temp = int(str(temp)[1:-1])
                if temp == 2 or temp == 3 or temp == 5 or (temp == 7):
                    primes.append(num)
    return sorted(list(set(primes)), reverse=True)