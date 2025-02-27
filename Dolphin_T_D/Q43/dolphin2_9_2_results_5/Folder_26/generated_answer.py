def find_primes_between_indices(numbers):
    primes_between = []
    for num in numbers[23:48]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes_between.append(num)
    return sorted(primes_between)