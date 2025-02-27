from typing import List

def find_primes_between_indices(int_list: List[int], start: int=52, end: int=53) -> List[int]:
    """

    Function that takes one argument, a list of integers, and returns the sorted list of all prime numbers from index 52 to index 53, both inclusive. The returned list should be in ascending order. If no prime number exists in the specified range, the function should return an empty list.

    """
    prime_list = []
    for num in int_list:
        if num >= start and num <= end:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    prime_list.sort()
    return prime_list if prime_list else []