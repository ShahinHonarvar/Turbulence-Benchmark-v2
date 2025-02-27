def all_right_truncatable_prime(nums):
    x = nums[0]
    prime_numbers = [2, 3, 5, 7]
    for num in range(10, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            if all((str(num)[j] != '0' for j in range(len(str(num))))):
                temp = str(num)
                while temp and int(temp) in prime_numbers:
                    temp = temp[:-1]
                if temp == '':
                    prime_numbers.append(num)
    return sorted(prime_numbers)