def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = []
    for num in range(2, x + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                num_str = str(num)
                is_truncatable = True
                while len(num_str) > 1:
                    if not (int(num_str) > 1 and all((int(digit) != 0 for digit in num_str))):
                        is_truncatable = False
                        break
                    num_str = num_str[1:]
                    if not (int(num_str) > 1 and all((int(digit) != 0 for digit in num_str))):
                        is_truncatable = False
                        break
                    num_str = num_str[:-1]
                if is_truncatable:
                    primes.append(num)
    return sorted(primes, reverse=True)