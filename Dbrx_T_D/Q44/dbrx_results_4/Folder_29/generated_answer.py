def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 52 and i <= 71:
            num = numbers[i]
            if num > 1 and (not is_prime(num)):
                composite_numbers.add(num)
    return composite_numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True