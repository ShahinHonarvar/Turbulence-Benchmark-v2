def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[77]
    if x < 10:
        return []
    numbers = list(range(x, 1, -1))
    while numbers[-1] > 1:
        if numbers[-1] % 10 != 0:
            if all((is_prime(int(str(numbers[-1])[i:])) for i in range(1, len(str(numbers[-1]))))):
                numbers = numbers[:-1]
            else:
                numbers = numbers[:-1]
                numbers.append(numbers[-1] - 1)
        else:
            numbers = numbers[:-1]
            numbers.append(numbers[-1] - 1)
    return numbers