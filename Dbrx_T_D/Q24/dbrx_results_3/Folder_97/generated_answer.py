def sum_of_divisors_in_range(n: int) -> int:

    def sum_of_divisors(k: int) -> int:
        total = 1
        for i in range(2, int(k ** 0.5) + 1):
            if k % i:
                continue
            total += i
            if i != k // i:
                total += k // i
        return total
    return sum((sum_of_divisors(d) for d in range(1, n + 1) if 615 <= sum_of_divisors(d) <= 792))