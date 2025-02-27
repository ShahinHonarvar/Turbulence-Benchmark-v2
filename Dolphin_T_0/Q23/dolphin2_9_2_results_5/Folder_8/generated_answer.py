def find_divisors_in_range(N):
    divisors = []
    i = 1
    while i <= N / 2:
        if N % i:
            divisors.append(i)
        i += 1
    return [d for d in divisors if 48 <= d <= 62]