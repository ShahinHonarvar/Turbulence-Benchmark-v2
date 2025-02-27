def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    result_set = set()
    valid_chars = [c for c in s if c.isalpha()]
    for i in range(len(valid_chars) - 2):
        sub_three = valid_chars[i:i + 3]
        if sub_three == sub_three[::-1]:
            result_set.add(''.join(sub_three))
    for i in range(len(valid_chars) - 3):
        sub_four = valid_chars[i:i + 4]
        if sub_four == sub_four[::-1]:
            result_set.add(''.join(sub_four))
    return result_set