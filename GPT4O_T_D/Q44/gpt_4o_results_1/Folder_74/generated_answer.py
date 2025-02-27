def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 1:
            return False
        if n <= 3:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    composites = set()
    for idx in range(42, 69):
        if idx < len(numbers) and is_composite(numbers[idx]):
            composites.add(numbers[idx])
    return composites