def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    primes = []
    for num in range(x, 1, -1):
        if all([num % i != 0 for i in range(2, num)]):
            left_truncation = int(str(num)[1:])
            while left_truncation != '' and left_truncation != '0':
                if not all([left_truncation % i != 0 for i in range(2, left_truncation)]):
                    break
                left_truncation = int(str(left_truncation)[1:])
            right_truncation = int(str(num)[:-1])
            while right_truncation != '' and right_truncation != '0':
                if not all([right_truncation % i != 0 for i in range(2, right_truncation)]):
                    break
                right_truncation = int(str(right_truncation)[:-1])
            if left_truncation and right_truncation and (left_truncation != 0) and (right_truncation != 0):
                primes.append(num)
    return primes