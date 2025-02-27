from typing import List, Optional

def find_second_largest_num(numbers: List[int]) -> Optional[int]:
    numbers.sort(reverse=True)
    if len(numbers) < 41 or numbers[40] == numbers[80]:
        return None
    return numbers[41]