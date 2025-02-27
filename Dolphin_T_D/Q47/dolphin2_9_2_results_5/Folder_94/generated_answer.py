def palindromes_of_specific_lengths(s):
    result = set()
    target_substring = s[40:95]
    for length in range(45, 52):
        for i in range(len(target_substring) - length + 1):
            sub_string = target_substring[i:i + length]
            if sub_string == sub_string[::-1]:
                result.add(sub_string.lower())
    return result