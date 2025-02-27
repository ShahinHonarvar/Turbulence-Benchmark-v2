from typing import Any

def find_second_largest_num(numbers: list[int]) -> Any:
    if not numbers or len(numbers) < 2:
        return None
    if 56 > len(numbers) or len(numbers) > 82:
        return None
    numbers.sort(reverse=True)
    if len(numbers) < 57 or numbers[56] == numbers[57]:
        return None
    return numbers[57]