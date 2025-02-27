def composite_nums_between_indices(numbers):

    def is_composite(n):
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
    composite_numbers = set()
    for i in range(75, 95):
        if i < len(numbers) and is_composite(numbers[i]):
            composite_numbers.add(numbers[i])
    return composite_numbers