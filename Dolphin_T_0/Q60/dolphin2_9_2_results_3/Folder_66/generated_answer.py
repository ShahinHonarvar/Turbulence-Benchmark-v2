def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    primes = [2, 3, 5, 7]
    for number in range(x, 1, -1):
        digits = [int(d) for d in str(number)]
        if 0 in digits:
            continue
        for _ in range(len(digits)):
            if number // 10 ** (len(digits) - 1) % 10 != number % 10:
                break
            number //= 10
            if number < 10:
                continue
        else:
            primes.append(number)
    return list(sorted(primes, reverse=True))