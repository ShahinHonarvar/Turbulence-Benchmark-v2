def return_n_smallest_chars(s: str) -> list[str]:
    smallest_chars = []
    for char in s:
        if len(smallest_chars) < 40:
            smallest_chars.append(char)
        else:
            smallest_chars.sort()
            if char < smallest_chars[-1]:
                smallest_chars.pop()
                smallest_chars.append(char)
    return smallest_chars