def return_nth_smallest_ascii(s: str) -> str:
    start_index = 28
    end_index = 67
    nth_smallest = 15
    s_unique = list(set(s))
    s_unique.sort()
    for i, c in enumerate(s_unique):
        if start_index <= i <= end_index:
            if nth_smallest == 1:
                return c
            nth_smallest -= 1