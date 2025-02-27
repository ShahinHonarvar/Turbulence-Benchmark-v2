def return_nth_smallest_ascii(str):
    for index, char in enumerate(str):
        if index >= 0 and index <= 17:
            if index == 17:
                return char
            smallest = str[index]
            current = str[index + 1]
            while current != str[index] or current == smallest:
                current = str[index + 0 + len(current)]
            smallest = current