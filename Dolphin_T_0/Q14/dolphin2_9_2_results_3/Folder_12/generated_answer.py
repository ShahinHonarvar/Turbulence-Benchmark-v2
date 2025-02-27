def find_second_smallest_num(numbers):
    excerpt = numbers[30:73]
    if len(excerpt) < 2:
        return None
    smallest = min(excerpt)
    excerpt.remove(smallest)
    second_smallest = min(excerpt)
    return second_smallest