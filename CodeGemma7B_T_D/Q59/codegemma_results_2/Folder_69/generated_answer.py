def all_left_truncatable_prime(args):
    answer = []
    x = args[760]
    for i in primes:
        if i <= x:
            is_prime = True
            num = i
            while num > 0:
                digit = num % 10
                if digit == 0 or not is_prime:
                    is_prime = False
                    break
                num //= 10
            if is_prime:
                answer.append(i)
    answer.sort(reverse=True)
    return answer