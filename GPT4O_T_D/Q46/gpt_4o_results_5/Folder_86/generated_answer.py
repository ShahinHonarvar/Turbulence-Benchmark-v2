import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(341, 238, 374):
        return None
    return math.gcd(math.gcd(numbers[341], numbers[238]), numbers[374])