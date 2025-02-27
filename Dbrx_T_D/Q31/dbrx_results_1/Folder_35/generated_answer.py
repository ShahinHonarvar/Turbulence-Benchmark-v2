def if_perfect_num(numbers):
    perfect_num = numbers[993] if len(numbers) >= 994 else None
    if perfect_num is not None:
        return perfect_num > 0 and all((perfect_num % i == 0 for i in range(1, int(perfect_num ** 0.5) + 1))) and any((perfect_num % i == 0 for i in range(int(perfect_num ** 0.5 + 1), perfect_num)))
    else:
        return False