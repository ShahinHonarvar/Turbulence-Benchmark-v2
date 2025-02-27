def all_right_truncatable_prime(numbers):
    prime = numbers[96]
    temp = prime
    prime_list = []
    while temp:
        if is_prime(temp):
            prime_list.append(temp)
        temp = temp // 10
    if prime_list == []:
        return []
    prime_list = sorted(prime_list, reverse=True)
    for i in range(len(prime_list)):
        if not is_right_truncatable(prime_list[i], prime_list[i - 1:]):
            prime_list.remove(prime_list[i])
    return prime_list

def is_right_truncatable(n, prime_list):
    while n:
        if n % 10 in [2, 3, 5, 7]:
            if not is_prime(n):
                return False
            else:
                n = n // 10
        else:
            n = int(str(n).rstrip(str(n[-1])))
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True