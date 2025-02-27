def return_n_smallest_chars(input_string):
    input_ord = [ord(char) for char in input_string]
    input_ord.sort()
    result = []
    for i in range(43):
        result.append(chr(input_ord[i]))
    result.sort(reverse=True)
    return result