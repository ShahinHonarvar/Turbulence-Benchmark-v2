def sum_of_divisors_in_range(num):
    """
  This function calculates the sum of all positive divisors of a number that are in the range of 586 to 840 (inclusive).
  
  Parameters:
  num: The number to calculate the sum of divisors for.
  
  Returns:
  The sum of all positive divisors of the number that are between 586 and 840, or 0 if no such divisors exist.
  """
    divisors = []
    for i in range(586, 841):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)