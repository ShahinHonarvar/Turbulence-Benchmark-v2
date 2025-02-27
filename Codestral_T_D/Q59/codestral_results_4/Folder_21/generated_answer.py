def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            flag = True
            while num > 0:
                num = int(str(num)[1:])
                if num > 0:
                    if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                        continue
                    else:
                        flag = False
                        break
            if flag:
                primes.append(num)
    return sorted(primes)