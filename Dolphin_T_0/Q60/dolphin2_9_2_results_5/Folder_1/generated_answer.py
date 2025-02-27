def is_prime(n):
    if n == 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    truncatables = []
    for n in range(x, 1, -1):
        if is_prime(n):
            n = str(n)
            l = len(n)
            if all((int(n[i:j]) != 0 and is_prime(int(n[i:j])) for i in range(l) for j in range(i + 1, l + 1))):
                truncatables.append(n)
    return sorted(truncatables, key=int, reverse=True)