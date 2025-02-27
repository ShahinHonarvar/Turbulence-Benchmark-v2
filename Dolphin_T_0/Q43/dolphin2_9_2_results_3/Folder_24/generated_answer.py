def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def find_primes_between_indices(nums):
    output = []
    for i in range(38, 56):
        if is_prime(nums[i]):
            output.append(nums[i])
    output.sort(reverse=True)
    return output