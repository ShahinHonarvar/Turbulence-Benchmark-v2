def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in range(2, numbers[28] + 1):
        number_list = list(map(int, str(number)))
        start = 0
        while len(number_list) > 1:
            if 0 in number_list:
                break
            number_list.pop(start)
            number_list.pop(-1)
            new_number = int(''.join(map(str, number_list)))
            if new_number < 2:
                break
            if all((new_number % n != 0 for n in range(2, int(new_number ** 0.5) + 1))):
                start += 1
        else:
            primes.append(number)
    return sorted(primes)