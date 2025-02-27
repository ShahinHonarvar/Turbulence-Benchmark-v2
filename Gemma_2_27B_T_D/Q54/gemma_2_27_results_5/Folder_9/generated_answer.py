def all_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for num in range(x, 1, -1):
        prime = True
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                prime = False
                break
        if prime:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True