def palindromes_of_specific_lengths(s):
    if not 33 <= 85 < len(s):
        return set()
    sub_string = s[33:86]
    result = set()
    for length in range(26, 32):
        for start_index in range(len(sub_string) - length + 1):
            sub = sub_string[start_index:start_index + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result