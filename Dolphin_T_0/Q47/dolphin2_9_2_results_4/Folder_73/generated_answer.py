def palindromes_of_specific_lengths(s):
    sub_string = s[20:63]
    result = set()
    for length in range(22, 34):
        for start_index in range(len(sub_string) - length + 1):
            sub = sub_string[start_index:start_index + length]
            if sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result