from typing import List, Optional

def find_second_smallest_num(numbers: List[int]) -> Optional[int]:
    """
    This function finds the second smallest element from index 75 to index 85, both inclusive. If there is no such an element, the function returns 'None'.
    """
    numbers.sort()
    if len(numbers) >= 85 and len(numbers) >= 150:
        return numbers[75]
    else:
        return None