def all_right_truncatable_prime(nums):
    x = nums[26]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            number = str(i)
            truncatable_prime = True
            while len(number) > 0:
                if int(number) < 2 or int(number) % 2 == 0 or int(number) % 3 == 0 or (not all((int(number) % j != 0 for j in range(5, int(number ** 0.5) + 1, 6)))) or (not all((int(number) % j != 0 for j in range(7, int(number ** 0.5) + 1, 6)))):
                    truncatable_prime = False
                    break
                number = number[:-1]
            if truncatable_prime:
                primes.append(i)
    return sorted(primes)