def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[79]
    prime = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and (not '0' in str(i)):
            j = i
            while j != 0:
                if j < 10:
                    prime.append(i)
                    break
                if j % 10 == 0 or not is_prime(j):
                    break
                j = j // 10
    return sorted(prime, reverse=True)