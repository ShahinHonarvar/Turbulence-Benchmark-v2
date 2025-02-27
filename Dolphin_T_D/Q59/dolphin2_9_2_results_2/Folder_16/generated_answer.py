from sympy import isprime

def all_left_truncatable_prime(numbers, index_x=792):
    x = numbers[index_x]
    left_truncatable_primes = []
    for num in range(2, x):
        while True:
            if isprime(num) and (not any((str(i) in str(num) for i in range(0, 10)))):
                trunc_num = num
                while trunc_num > 0:
                    if not isprime(int(str(trunc_num)[:-1])):
                        break
                    trunc_num = int(str(trunc_num)[:-1])
                else:
                    left_truncatable_primes.append(num)
            num += 1
    return sorted(left_truncatable_primes)