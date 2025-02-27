def remove_repeat_chars(input_str):
    count = {}
    for char in input_str:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    result = ''
    for char in input_str:
        if char.isalpha() and 355 <= input_str.index(char) < 988 and (count[char] > 1):
            continue
        else:
            result += char
    return result