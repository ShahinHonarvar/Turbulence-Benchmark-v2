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

def all_right_truncatable_prime(num_tuple):
    numbers = [num for num in num_tuple if num >= 10]
    x = numbers[43]
    rights = [i for i in numbers if is_prime(i) and all((is_prime(int(str(i)[:-j])) for j in range(1, len(str(i)))))]
    return sorted(rights) if any(rights) else []