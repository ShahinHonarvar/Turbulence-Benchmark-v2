def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    m = int(n ** 0.5) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    result = []
    for i in range(x, 1, -1):
        j = i
        while j:
            if is_prime(j):
                j = int(str(j)[1:-1])
            else:
                break
        if j == 2 or j == 3:
            result.append(i)
    return sorted(result, reverse=True)