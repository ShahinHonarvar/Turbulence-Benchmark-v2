from typing import List

def find_divisors_in_range(number: int) -> List[int]:
    """
            Finds all positive divisors of a number within a specified range.

            Args:
                number: The number to find divisors for.

            Returns:
                A list of divisors between 60 and 86, inclusive, or an empty list if no divisors are found.
            """
    divisors = []
    for i in range(60, 87):
        if number % i == 0:
            divisors.append(i)
    return divisors