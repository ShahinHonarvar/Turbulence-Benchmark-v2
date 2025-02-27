def palindrome_of_length_at_least_n(input_string):
    result = set()
    str_lower = input_string.replace(' ', '').lower()
    for i in range(len(str_lower)):
        for j in range(i + 2, len(str_lower) + 1):
            subs = str_lower[i:j]
            if subs == subs[::-1] and len(subs) >= 68:
                result.add(subs)
    return result