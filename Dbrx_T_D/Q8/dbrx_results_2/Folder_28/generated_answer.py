def all_even_ints_exclusive(n: [int]) -> [int]:
    return [num for num in n[20:51] if num in range(2, 50) and num % 2 == 0]