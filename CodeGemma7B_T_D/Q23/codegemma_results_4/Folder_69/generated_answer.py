def find_divisors_in_range(num):
    """Return the list of all positive divisors of num
  that are between 658 and 868 both inclusive,
  if no such divisors exist, return an empty list."""
    divisors = []
    for divisor in range(658, 868):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors