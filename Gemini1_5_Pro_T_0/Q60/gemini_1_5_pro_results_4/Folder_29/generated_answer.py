def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in [2, 3, 5, 7, 11, 13, 17, 23, 37, 53, 73, 313, 317, 797] and int(str(num)[i:]) in [2, 3, 5, 7, 11, 13, 17, 23, 37, 53, 73, 313, 317, 797] for i in range(1, len(str(num))))):
            result.append(num)
    result.sort(reverse=True)
    return result